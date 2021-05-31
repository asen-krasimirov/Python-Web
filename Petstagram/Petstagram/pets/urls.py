from django.urls import path
from Petstagram.pets import views

urlpatterns = [
    path('', views.all_pets, name="all pets"),
    path('details/<pk>', views.pet_details, name="pet details"),
    path('like/<pk>', views.like_pet, name="like pet"),
]
