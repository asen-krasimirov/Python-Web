from django.shortcuts import render, redirect
from Petstagram.pets.models import Pet, Like


def all_pets(request):
    pet_data = Pet.objects.all()

    for index, pet in enumerate(pet_data):
        pet_data[index].details_url = f"details/{pet.pk}"

    return render(request, 'pets/pet_list.html', {"pet_data": pet_data})


def pet_details(request, pk):
    pet_info = Pet.objects.get(pk=pk)
    like_count = Like.objects.all().filter(pet=pk).count()

    pet_info.like_url = f"../like/{pk}"

    return render(request, 'pets/pet_detail.html', {"pet_info": pet_info, "like_count": like_count})


def like_pet(request, pk):
    Like(
        pet=Pet.objects.get(pk=pk)
    ).save()

    return redirect(f"../details/{pk}")
