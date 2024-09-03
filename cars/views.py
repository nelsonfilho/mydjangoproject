from django.shortcuts import render
from .models import Car
from django.http import QueryDict


def car_view(request):
    cars = Car.objects.all().order_by('model')
    try: 
        query_key = next(iter(request.GET.keys()))
        if query_key:
            search = request.GET.get(query_key)
            filter_kwargs = {f'{query_key}__icontains': search}
            cars = Car.objects.filter(**filter_kwargs).order_by('query_key')
    except:
        pass
    return render(request, 'cars.html', context={'cars': cars})