from django.shortcuts import render, redirect
from .models import Car
from cars.forms import CarForm
from django.http import QueryDict
from Scripts import clean_str

def car_view(request):
    cars = Car.objects.all().order_by('model')
    try:
        query_key = next(iter(request.GET.keys()))
        search = request.GET.get(query_key)
        print(f'testing {Car.objects.model}')
        if query_key == 'search':

            if Car.objects.filter(model__icontains=search):
                filter_kwargs = {f'models__icontains': search}
                cars = Car.objects.filter(model__icontains=search).order_by('model')
            else:
                filter_kwargs = {f'brand__name__icontains': search}
                cars = Car.objects.filter(brand__name__icontains=search).order_by('brand')

        return render(request, 'cars_aula.html', context={'cars': cars})

    except:
        return render(request, 'cars_aula.html', context={'cars': cars})


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)
        print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        else:
            print(new_car_form.errors)
    else:
        new_car_form = CarForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})
