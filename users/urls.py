from django.urls import path, re_path

from . import views

urlpatterns = [
    path('explore/', views.users),
    # TODO: login/facebook/
    # path('login/facebook', views.follow)
    path('search/', views.users),
    path('<int:pk>/follow/', views.follow),
    path('<int:pk>/follow/', views.unfollow),
    path('<slug:username>', views.users_detail),
    path('<slug:username>/followers/', views.followers),
    path('<slug:username>/following/', views.following),
    # re_path(r'^([\w.@+-]+)/$', views.users_detail),
    # re_path(r'^([\w.@+-]+)/followers/$', views.followers),
    # re_path(r'^([\w.@+-]+)/following/$', views.following),
    # TODO: {username}/password/
]
