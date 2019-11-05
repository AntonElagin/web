from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Creator, Follow
from .serializers import CreatorSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework_social_oauth2.authentication import SocialAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from django.http import HttpResponse






class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


@api_view(['GET'])
def user(request):
    pass


@api_view(['GET'])
# Поиск по username
def users(request):
    request.user.get_username()
    if request.method == 'GET':
        if 'search' in request.GET:
            search = request.GET['search']
            search_users = Creator.objects.filter(user__username=search)
        else:
            search_users = Creator.objects.all()
        serializer = CreatorSerializer(search_users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
# Детали user
def users_detail(request, username):
    if request.method == 'GET':
        user = get_object_or_404(Creator, user__username=username)
        serializer = CreatorSerializer(user)
        return Response(serializer.data)


@authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
@api_view(['POST'])
# Подписка
def follow(request, pk):
    if request.method == 'POST':
        idol = get_object_or_404(Creator, pk=pk)
        Follow.objects.create(author=idol, follower=request.user)
        return Response(status=status.HTTP_201_CREATED)

@authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
@api_view(['GET'])
def followers(request, username):
    if request.method == 'GET':
        idol = Creator.objects.get(user__username=username)
        follows = Follow.objects.filter(author=idol)
        followers_list = []
        for follow in follows:
            serializer = CreatorSerializer(follow.follower)
            followers_list.append(serializer.data)
        return Response(followers_list)


@authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
@api_view(['GET'])
def following(request, username):

    if request.method == 'GET':
        user = Creator.objects.get(user__username=username)
        follows = Follow.objects.filter(follower=user)
        following_list = []
        for follow in follows:
            serializer = CreatorSerializer(follow.author)
            following_list.append(serializer.data)
        return Response(following_list)


@authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
@api_view(['DELETE'])
# Отписка
def unfollow(request, pk):
    idol = get_object_or_404(Creator, pk=pk)
    follow_obj = Follow.objects.get(author=idol, follower=request.user)
    if request.method == 'DELETE':
        follow_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



