import os
from django.db import models
from django.dispatch import receiver
from uuid import uuid4


def image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = "animal_%s.%s" % (uuid4().hex, ext)
    return 'animals/' + new_filename


class AnimalType(models.Model):
    value = models.CharField("Wartość", max_length=100,
                             unique=True, null=False)

    def __str__(self):
        return str(self.value)


class AnimalBreed(models.Model):
    value = models.CharField("Wartość", max_length=100,
                             unique=True, null=False)

    def __str__(self):
        return str(self.value)


class AnimalGender(models.Model):
    value = models.CharField("Wartość", max_length=100,
                             unique=True, null=False)

    def __str__(self):
        return str(self.value)


class AnimalStatus(models.Model):
    value = models.CharField("Wartość", max_length=100,
                             unique=True, null=False)

    def __str__(self):
        return str(self.value)


class Animal(models.Model):
    chip_code = models.CharField(
        "Chip Code", max_length=100, unique=True, null=False)
    name = models.CharField("Imię", max_length=100)
    age = models.PositiveSmallIntegerField("Pełnych lat")
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    animal_breed = models.ForeignKey(AnimalBreed, on_delete=models.CASCADE)
    animal_gender = models.ForeignKey(AnimalGender, on_delete=models.CASCADE)
    color = models.TextField("Kolor", max_length=500,
                             help_text="Opisanie koloru")
    image = models.ImageField(upload_to=image_path, default='animals/default.jpg')
    height = models.PositiveSmallIntegerField("Wzrost")
    weight = models.PositiveSmallIntegerField("Masa")
    description = models.TextField("Komentarz", max_length=1000)
    vaccinations = models.TextField(
        "Szczepienia", max_length=1000, help_text="Tu opisz jakie szczepienia miało")
    animal_status = models.ForeignKey(
        AnimalStatus, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.name) + " " + str(self.chip_code)


class AnimalImage(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=False, related_name="images")
    image = models.ImageField(upload_to=image_path, null=False)


def _delete_file(path):
   if os.path.isfile(path):
       os.remove(path)


@receiver(models.signals.post_delete, sender=AnimalImage)
def delete_file(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_file(instance.image.path)


@receiver(models.signals.post_delete, sender=Animal)
def delete_file(sender, instance, *args, **kwargs):
    if instance.image:
        _delete_file(instance.image.path)
    if instance.images:
        for image in instance.images.all(): 
            _delete_file(image.path)
