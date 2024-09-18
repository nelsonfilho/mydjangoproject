from typing import Any
from django import forms
from cars.models import Brand, Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self) -> dict[str, Any]:
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('Valor minimo do carro deve ser de R$20.000')
        return value