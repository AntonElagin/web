from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Image, Comment, Like
from users.models import Creator
from .serializers import ImageSerializer, CommentSerializer, LikeSerializer
from rest_framework_social_oauth2.authentication import SocialAuthentication
# from oauth2_provider.contrib.rest_framework import A
from users.views import CsrfExemptSessionAuthentication
from django.shortcuts import get_object_or_404, get_list_or_404


@api_view(['GET'])
@authentication_classes(
    [CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def images(request):
    if request.method == 'GET':
        creator = get_object_or_404(Creator, id=request.user.id)
        # creator = Creator.objects.get(id=request.user.id)
        images = []
        try:
            images = Image.objects.filter(creator=creator)
        except:
            pass

        # Paginator
        paginator = Paginator(images, 20)
        if 'page' in request.GET:
            page_number = request.GET['page']
        else:
            page_number = 1
        page = paginator.get_page(page_number)
        previous_page = page.previous_page_number() if page.has_previous() else 1
        next_page = page.next_page_number() if page.has_next() else 1

        serializer = ImageSerializer(page.object_list, many=True)
        return Response({'data': serializer.data,
                         'page': page_number,
                         'previous': previous_page,
                         'next': next_page,
                         'num_pages': paginator.num_pages})


@api_view(['GET', 'POST'])
@authentication_classes(
    [CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def images_post(request):
    creator = get_object_or_404(Creator, id=request.user.id)
    # creator = Creator.objects.get(id=request.user.id)
    if request.method == 'GET':
        images = []
        try:
            images = Image.objects.filter(creator=creator)
        except:
            pass
        # Paginator
        paginator = Paginator(images, 20)

        if 'page' in request.GET:
            page_number = request.GET['page']
        else:
            page_number = 1
        page = paginator.get_page(page_number)
        previous_page = page.previous_page_number() if page.has_previous() else 1
        next_page = page.next_page_number() if page.has_next() else 1

        serializer = ImageSerializer(page.object_list, many=True)
        return Response({'data': serializer.data,
                         'page': page_number,
                         'previous': previous_page,
                         'next': next_page,
                         'num_pages': paginator.num_pages})

    if request.method == 'POST':
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.creator_id = creator.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes(
    [CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def images_detail(request, image_pk):
    image = get_object_or_404(Image, id=image_pk)
    # image = Image.objects.get(pk=image_pk)
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
@authentication_classes(
    [CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def comments(request, image_pk):
    if request.method == 'POST':
        creator = get_object_or_404(Creator, id=request.user.id)
        # creator = Creator.objects.get(id=request.user.id)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.creator_id = creator.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes(
    [ BasicAuthentication])
@permission_classes([IsAuthenticated])
def comments_detail(request, image_pk, comment_pk):
    comment = get_object_or_404(Comment, id = comment_pk)
    # comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes(
    [CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([AllowAny])
def likes(request, image_pk):
    if request.method == 'GET':
        image = get_object_or_404(Image, id=image_pk)
        # image = Image.objects.get(pk=image_pk)
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
@authentication_classes(
    [CsrfExemptSessionAuthentication, BasicAuthentication])
@permission_classes([AllowAny])
def likes_detail(request, pk):
    like = get_object_or_404(Like, id=pk)
    # like = Like.objects.get(pk=pk)

    if request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
