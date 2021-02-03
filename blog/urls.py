from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,TeamDetailView
from users.views import PlayerDetailView
urlpatterns=[
	path('matches/',views.matches,name='match-play'),
	path('',PostListView.as_view(),name='blog-home'),
	path('teams/',views.teams,name='team-about'),
	path('points/',views.points,name='team-points'),
    path('teams/<int:pk>/',TeamDetailView.as_view(),name='team-detail'),
	path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
	path('player/<int:pk>/',PlayerDetailView.as_view(),name='player-detail'),
	path('post/new/',PostCreateView.as_view(),name='post-create'),
	path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
	path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
	path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
]
