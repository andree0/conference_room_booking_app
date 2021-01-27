from datetime import datetime

from django import forms
from django.utils.translation import gettext_lazy as _


from .models import Room, BookingRoom


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
        model = BookingRoom
        fields = ('date_of_booking', 'id_room', 'comment')
        labels = {
            'date_of_booking': _('Data rezerwacji'),
            'id_room': _('Sala konferencyjna'),
            'comment': _('Komentarz')
        }

        widgets = {
            'date_of_booking': forms.SelectDateWidget(),
            'id_room': forms.Select(choices=Room.objects.all().values_list('name')),
        }