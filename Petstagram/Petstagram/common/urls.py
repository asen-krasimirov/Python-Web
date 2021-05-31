from django.urls import path
from Petstagram.common import views


urlpatterns = [
    path('', views.landing_page, name='landing'),
]