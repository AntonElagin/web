from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Creator, Follow
from .serializers import CreatorSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework_social_oauth2.authentication import SocialAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


@api_view(['GET'])
def user_details(request):
    pass


@api_view(['GET'])
# Поиск по search
def users_search(request):

    if request.method == 'GET':
        if 'search' in request.GET:
            search = request.GET['search']
            # search_users = Creator.objects.filter(username=search)
            search_users =get_list_or_404(Creator, username=search)
        else:
            search_users = Creator.objects.all()
        serializer = CreatorSerializer(search_users, many=True)
        return Response(serializer.data)


# Детали user
@api_view(['GET'])
def users_details(request, username):

    if request.method == 'GET':
        user = get_object_or_404(Creator, username=username)
        serializer = CreatorSerializer(user)
        return Response(serializer.data)


# Подписка
@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
def follow(request, user_pk):
    if request.method == 'POST':
        idol = get_object_or_404(Creator, pk=user_pk)
        follower = get_object_or_404(Creator, id=request.user.id)
        # follower = Creator.objects.get(username=request.user) # TODO : затестить
        Follow.objects.create(author=idol, follower=follower)
        return Response(status=status.HTTP_201_CREATED)


# Подписчики
@api_view(['GET'])
@authentication_classes([CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
def followers(request, username):

    if request.method == 'GET':
        idol = get_object_or_404(Creator, username=username)
        # idol = Creator.objects.get(sername=username)
        follows = get_list_or_404(Follow, author=idol)
        # follows = Follow.objects.filter(author=idol)
        followers_list = []
        for follow in follows:
            serializer = CreatorSerializer(follow.follower)
            followers_list.append(serializer.data)
        return Response(followers_list)


# Подписчики
@api_view(['GET'])
def following(request, username):

    if request.method == 'GET':
        user = get_object_or_404(Creator, username=username)
        # user = Creator.objects.get(username=username)
        follows = get_list_or_404(Follow,follower=user)
        # follows = Follow.objects.filter(follower=user)
        following_list = []
        for follow in follows:
            serializer = CreatorSerializer(follow.author)
            following_list.append(serializer.data)
        return Response(following_list)


# Отписка
@api_view(['DELETE'])
@authentication_classes([CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
def unfollow(request, user_pk):

    idol = get_object_or_404(Creator, id=user_pk)
    follower = get_object_or_404(Creator, id=request.user.id)
    # follower = Creator.objects.get(username=request.user)
    # follow_obj = Follow.objects.get(author=idol, follower=follower)
    follow_obj = get_object_or_404(Follow, author=idol, follower=follower)

    if request.method == 'DELETE':
        follow_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



