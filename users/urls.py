from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.user_details),
    path('explore/', views.users_search),
    path('search/', views.users_search),
    path('<int:user_pk>/follow/', views.follow),
    path('<int:user_pk>/unfollow/', views.unfollow),
    path('<slug:username>', views.users_details),
    path('<slug:username>/followers/', views.followers),
    path('<slug:username>/following/', views.following),
    # TODO: {username}/password/
]
