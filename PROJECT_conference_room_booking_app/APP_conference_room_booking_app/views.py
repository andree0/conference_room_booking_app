from django.shortcuts import render
from django.views.generic.base import View

from .forms import RoomForm
from .models import Room


def start_page(request):
    return render(request, 'base.html')


class AddNewRoomView(View):

    def get(self, request, *args, **kwargs):
        form = RoomForm()
        context = {
            'form': form,
        }
        return render(request, 'add_new_room.html', context=context)

    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)
        if form.is_valid():
            name_room = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            projector = form.cleaned_data['projector']
            new_room = Room.objects.create(name=name_room, capacity=capacity, projector=projector)
            message = f'Dodano sale konferencyjną: {new_room.name}'
        else:
            message = 'Niepoprawne dane'

        context = {
            'message': message,
        }
        return render(request, 'base.html', context=context)
