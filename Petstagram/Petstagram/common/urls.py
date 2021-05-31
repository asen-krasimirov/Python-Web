from django.urls import path
from Petstagram.common import views


urlpatterns = [
    path('', views.landin_page, name='landing'),
]