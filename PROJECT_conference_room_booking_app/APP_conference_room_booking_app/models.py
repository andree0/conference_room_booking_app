from django.core.validators import MinValueValidator
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    capacity = models.IntegerField(null=False,
                                   validators=[MinValueValidator(2, message='Wartośc musi być większa od dwóch'), ])
    projector = models.BooleanField(default=False)


class BookingRoom(models.Model):
    date_of_booking = models.DateField()
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('date_of_booking', 'id_room')
