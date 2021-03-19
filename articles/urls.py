from django.urls import path

from . import views
from .views import (
    ArticleListView,

    ArticleDetailView,


)

urlpatterns = [

    path('<int:pk>/',
         ArticleDetailView.as_view(), name='article_detail'),

    path('new/', views.article_create_view, name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('count/',views.num_post,name='numpost'),
    path('lasthourposts', views.lasthourposts, name='lasthourposts'),
    path('appearance', views.appearance, name='appearance'),


]