from django.db import models
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from animals.models import Animal
from users.models import User


class AnimalArrival(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Użytkownik")
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, verbose_name="Zwierzę")
    date = models.DateTimeField(default=timezone.now, verbose_name="Data")
    first_name_of_surrender = models.CharField("Imię osoby przyprowadzającej", max_length=50, null=True)
    last_name_of_surrender = models.CharField("Nazwisko osoby przyprowadzającej", max_length=50, null=True)
    address_of_surrender = models.CharField("Adres osoby przyprowadzającej", max_length=200, null=True)

    def __str__(self):
        return str(self.animal) + " " + str(self.date)

    class Meta:
        verbose_name = 'Przyprowadzenie Zwierzęcia'
        verbose_name_plural = 'Przyprowadzenia Zwierząt'

    def save(self, *args, **kwargs):
        try:
            return super(AnimalArrival, self).save(*args, **kwargs)
        except BaseException as e:
            raise ValidationError({ 'error': str(e).split('\n')[0] })
