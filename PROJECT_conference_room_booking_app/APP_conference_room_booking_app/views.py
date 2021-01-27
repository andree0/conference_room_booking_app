from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from .forms import RoomForm, BookingForm
from .models import Room, Booking


class StartPageView(View):

    def get(self, request):
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


class ListOfRoomsView(View):

    def get(self, request, message_2=None, *args, **kwargs):
        conference_rooms = Room.objects.all()
        if not conference_rooms:
            message = 'Brak dostępnych sal'
        else:
            message = 'Lista sal konferencyjnych'
        context = {
            'conference_rooms': conference_rooms,
            'message': message,
            'message_2': message_2,
        }
        return render(request, 'list_of_rooms.html', context)


class DeleteRoomView(View):

    def get(self, request, id_room):
        room = get_object_or_404(Room, pk=id_room)
        room.delete()
        message_2 = f"Usunięto sale: {room.name}"
        return ListOfRoomsView.get(self, request, message_2=message_2)


class ModifyRoomView(View):

    def get(self, request, id_room):
        room = Room.objects.get(pk=id_room)
        form = RoomForm(instance=room)
        context = {
            'form': form,
        }
        return render(request, 'modify_room.html', context)

    def post(self, request, id_room):
        room = Room.objects.get(pk=id_room)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room.name = form.cleaned_data['name']
            room.capacity = form.cleaned_data['capacity']
            room.projector = form.cleaned_data['projector']
            room.save()
            message_2 = f"Zmodyfikowano sale: {room.name}"
        else:
            message_2 = f'Niepoprawne dane, nie zmodyfikowano sali.'

        return ListOfRoomsView.get(self, request, message_2)


class ReserveRoomView(View):

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        context = {
            'form': form,
        }
        return render(request, 'add_new_room.html', context=context)

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            date_of_booking = form.cleaned_data['date_of_booking']
            id_room = form.cleaned_data['id_room']
            comment = form.cleaned_data['comment']
            new_booking = Booking.objects.create(date_of_booking=date_of_booking, id_room=id_room, comment=comment)
            booked_room = Room.objects.get(pk=id_room)
            message = f'Zarezerwowano sale: {booked_room.name} ' \
                      f'na dzień {new_booking.date_of_booking}'
        else:
            message = 'Niepoprawne dane'

        context = {
            'message': message,
        }
        return render(request, 'base.html', context=context)


class DetailsRoomView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
