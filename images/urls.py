from django.urls import path

from . import views

urlpatterns = [
    path('', views.images),
    path('search/', views.images),
    path('<int:pk>/', views.images_detail),
    path('<int:image_pk>/comments/', views.comments),
    path('<int:image_pk>/comments/<int:comment_pk>/', views.comments_detail),
    path('<int:image_pk>/likes/', views.likes),
    path('<int:pk>/unlikes/', views.likes),
]
