from django.urls import path
from . import views

urlpatterns = [
    path('new_post/', views.NewPostCreateAPIView.as_view(), name='new_post'),
    path('posts/', views.GetPostListView.as_view(), name='posts'),
    path('new_like/', views.NewLikeDislikeCreateAPIView.as_view(), name='new_like'),
]
