from django.urls import path

from posts.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, AboutView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='posts.list'),
    path('create/', PostCreateView.as_view(), name='posts.create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='posts.update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='posts.delete'),
    path('<int:pk>/', PostDetailView.as_view(), name='posts.detail'),
]
