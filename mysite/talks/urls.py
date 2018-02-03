from django.urls import path

from talks import views

urlpatterns = [
    path('', views.talks_list_view, name='talks_list'),
]
