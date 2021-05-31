from django.db import models


class Pet(models.Model):
    pet_types = [
        ("cat", "cat"),
        ("dog", "dog"),
        ("parrot", "parrot"),
    ]
    type = models.CharField(
        max_length=6,
        choices=pet_types,
    )

    name = models.CharField(
        max_length=6
    )

    age = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField()


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
