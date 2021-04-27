from django.urls import path
from .views import BlogListView, BLogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [

    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='postDelete'),
    path('post/new/', BlogCreateView.as_view(), name='newPost'),
    path('post/<int:pk>/', BLogDetailView.as_view(), name='postDetail'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='postEdit'),
    path('', BlogListView.as_view(), name='home'),

]