from django.shortcuts import render
from .models import Car


def car_view(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', context={'cars': cars})