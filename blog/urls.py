
from django.urls import path
from . import views
from .views import FileListView,FileDetailView,FileCreateView,FileUpdateView,FileDeleteView,add_comment_to_post


urlpatterns =[
    path('',FileListView.as_view(),name='blog-home'),
    path('files/<int:pk>/',FileDetailView.as_view(),name='file-detail'),
    path('files/new/',FileCreateView.as_view(),name='file-create'),
    path('files/<int:pk>/update/', FileUpdateView.as_view(), name='file-update'),
    path('files/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('files/<int:pk>/delete/', FileDeleteView.as_view(), name='file-delete'),


    path('about/',views.about,name='blog-about'),


]