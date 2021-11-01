from django.db import models
from django.utils import timezone
from animals.models import Animal
from users.models import User


class ReservationStatus(models.Model):
    value = models.CharField("Wartość", max_length=100,
                             unique=True, null=False, help_text="")

    def __str__(self):
        return self.value


class AnimalReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    reservation_status = models.ForeignKey(
        ReservationStatus, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return str(self.person) + str(self.animal) + str(self.date)