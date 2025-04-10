from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CharField


class Breed(models.Model):
    tiny = 'tiny'
    small = 'small'
    medium = 'medium'
    large = 'large'

    SIZE_CHOICE = [
        ('tiny', tiny),
        ('small', small),
        ('medium', medium),
        ('large', large)
    ]
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=6, choices=SIZE_CHOICE)
    friendliness  = models.IntegerField(validators=(
        MinValueValidator(1),
        MaxValueValidator(5)
    ))
    trainability  = models.IntegerField(validators=(
        MinValueValidator(1),
        MaxValueValidator(5)
    ))
    shedding_amount  = models.IntegerField(validators=(
        MinValueValidator(1),
        MaxValueValidator(5)
    ))
    exercise_needs  = models.IntegerField(validators=(
        MinValueValidator(1),
        MaxValueValidator(5)
    ))

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=255)
    favorite_toy = models.CharField(max_length=255)
