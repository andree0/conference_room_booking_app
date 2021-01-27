from datetime import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Room, Booking


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'capacity', 'projector')
        labels = {
            'name': _('Nazwa sali'),
            'capacity': _('Pojemność sali'),
            'projector': _('Rzutnik')
        }
        widgets = {
            'capacity': forms.NumberInput(attrs={
                'type': 'number',
                'min': '2'
            })
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date_of_booking', 'comment')
        labels = {
            'date_of_booking': _('Data rezerwacji'),
            'comment': _('Komentarz')
        }

        widgets = {
            'date_of_booking': forms.SelectDateWidget(),
        }
