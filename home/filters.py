import django_filters
from django_filters import widgets
from django import forms

from .models import Car


class CarFilter(django_filters.FilterSet):

    car_make = [
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Kia', 'Kia'),
        ('Mazda', 'Mazda'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Nissan', 'Nissan'),
        ('Opel', 'Opel'),
        ('Renault', 'Renault'),
        ('Skoda', 'Skoda'),
        ('Toyota', 'Toyota'),
        ('Tesla', 'Tesla'),
        ('Volkswagen', 'Volkswagen'),
    ]

    car_fuel_type = [
        ('benzyna', 'Benzyna'),
        ('diesel', 'Diesel'),
        ('hybryda', 'Hybryda'),
        ('elektryczny', 'Elektryczny'),
        ('lpg', 'LPG'),
    ]

    car_gear_type = [
        ('Manualna', 'Manualna'),
        ('Automatyczna', 'Automatyczna'),
    ]

    make = django_filters.MultipleChoiceFilter(
        choices=car_make,
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-actions-box': 'true'})
        )
    year = django_filters.RangeFilter(
        widget=widgets.RangeWidget(attrs={'class': 'form-control' ,'style': 'width: 45%; display: inline-block;'})
    )
    price = django_filters.RangeFilter(
        widget=widgets.RangeWidget(attrs={'class': 'form-control' ,'style': 'width: 45%; display: inline-block;'})
    )
    mileage = django_filters.RangeFilter(
        widget=widgets.RangeWidget(attrs={'class': 'form-control' ,'style': 'width: 45%; display: inline-block;'})
    )
    engine_capacity = django_filters.RangeFilter(
        widget=widgets.RangeWidget(attrs={'class': 'form-control' ,'style': 'width: 45%; display: inline-block;'})
    )
    engine_power = django_filters.RangeFilter(
        widget=widgets.RangeWidget(attrs={'class': 'form-control' ,'style': 'width: 45%; display: inline-block;'})
    )
    fuel_type = django_filters.MultipleChoiceFilter(
        choices=car_fuel_type,
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-actions-box': 'true'})
        )
    gear = django_filters.MultipleChoiceFilter(
        choices=car_gear_type,
        widget=forms.SelectMultiple(attrs={'class': 'selectpicker', 'data-live-search': 'true', 'data-actions-box': 'true'})
        )

    class Meta:
        model = Car
        fields = ['make', 'year', 'price', 'mileage', 'engine_capacity', 'engine_power', 'fuel_type', 'gear']

