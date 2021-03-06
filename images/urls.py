from django.urls import path

from . import views

urlpatterns = [
    path('', views.images_post),
    path('search/', views.images),
    path('<int:image_pk>/', views.images_detail),
    path('<int:image_pk>/comments/', views.comments),
    path('<int:image_pk>/comments/<int:comment_pk>/', views.comments_detail),
    path('<int:image_pk>/likes/', views.likes),
    path('<int:image_pk>/unlikes/', views.likes),
]
