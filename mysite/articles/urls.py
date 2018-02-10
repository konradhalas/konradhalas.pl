from django.urls import path

from articles import views

urlpatterns = [
    path('', views.articles_list_view, name='articles_list'),
    path('<str:slug>/', views.article_details_view, name='article_details'),
]
