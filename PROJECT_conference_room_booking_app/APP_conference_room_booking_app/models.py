from django.core.validators import MinValueValidator
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    capacity = models.IntegerField(null=False,
                                   validators=[MinValueValidator(2, message='Wartośc musi być większa od dwóch'), ])
    projector = models.BooleanField(default=False)


