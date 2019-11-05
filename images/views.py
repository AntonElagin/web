from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from social_django.models import UserSocialAuth
from django.contrib.auth.models import User
from .models import Image, Comment, Like
from users.models import Creator
from rest_framework_social_oauth2.authentication import SocialAuthentication
from .serializers import ImageSerializer, CommentSerializer, LikeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework_social_oauth2.authentication import SocialAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from users.views import CsrfExemptSessionAuthentication


from django.http import HttpResponse



@api_view(['GET', 'POST'])
@authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([AllowAny])
@csrf_exempt
def images(request):

    user = User.objects.get(username=request.user.get_username())
    # return HttpResponse(user.email)

    creator = Creator.objects.get_or_create(user=user,name=str(user.first_name+user.last_name))
    # creator = Creator.objects.get(user__username=user)
    # return HttpResponse(str(creator))
    if request.method == 'GET':

        images = Image.objects.filter(creator=creator[0])

        # Paginator
        paginator = Paginator(images, 20)

        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        previous_page = page.previous_page_number() if page.has_previous() else 1
        next_page = page.next_page_number() if page.has_next() else 1

        serializer = ImageSerializer(page.object_list, many=True)
        return Response({'data': serializer.data,
                         'page': page_num,
                         'previous': previous_page,
                         'next': next_page,
                         'num_pages': paginator.num_pages})

    if request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.creator_id = creator[0].id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def images_detail(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comments(request, image_pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.creator_id = creator.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def comments_detail(request, image_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([AllowAny])
def likes(request, image_pk):
    if request.method == 'GET':
        image = Image.objects.get(pk=image_pk)
        likes = image.like_set
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([OAuth2Authentication, SocialAuthentication, CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([AllowAny])
def likes_detail(request, pk):
    like = Like.objects.get(pk=pk)
    if request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
