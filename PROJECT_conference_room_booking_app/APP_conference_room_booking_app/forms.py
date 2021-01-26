from django import forms
from django.utils.translation import gettext_lazy as _


from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name', 'capacity', 'projector')
        labels = {'name': _('Nazwa sali'), 'capacity': _('Pojemność sali'), 'projector': _('Rzutnik')}
        widgets = {
            'capacity': forms.NumberInput(attrs={
                            'type': 'number',
                            'min': '2'
                        })
                        }

# class BookingForm(forms.Form):
