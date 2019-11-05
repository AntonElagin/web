from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.user),
    path('explore/', views.users),
    path('search/', views.users),
    path('<int:pk>/follow/', views.follow),
    path('<int:pk>/unfollow/', views.unfollow),
    path('<slug:username>', views.users_detail),
    path('<slug:username>/followers/', views.followers),
    path('<slug:username>/following/', views.following),
    # TODO: {username}/password/
]
