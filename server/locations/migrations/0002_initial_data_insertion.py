# Generated by Django 3.2.8 on 2021-11-08 11:28

from django.db import migrations
from django.utils import timezone
from faker import Faker
from faker.providers import date_time

fake = Faker()
fake.add_provider(date_time)


def insert_buildings(apps, schema_editor):
    Building = apps.get_model('locations', 'Building')
    for _ in range(2):
        street = 'Wrocaw, Sowacka 11'
        number = fake.pyint(min_value=0, max_value=120)
        Building.objects.create(street=street, number=number)


def insert_rooms(apps, schema_editor):
    Building = apps.get_model('locations', 'Building')
    Room = apps.get_model('locations', 'Room')
    for _ in range(5):
        capacity = fake.pyint(min_value=0, max_value=20)
        number = fake.pyint(min_value=0, max_value=120)
        building = Building.objects.order_by('?').first()
        Room.objects.create(capacity=capacity,
                            number=number, building=building)


def insert_locations(apps, schema_editor):
    Animal = apps.get_model('animals', 'Animal')
    Room = apps.get_model('locations', 'Room')
    AnimalLocation = apps.get_model('locations', 'AnimalLocation')

    for animal in Animal.objects.all():
        room = Room.objects.order_by('?').first()
        AnimalLocation.objects.create(
            room=room, animal=animal)


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('users', '0002_initial_data_insertion'),
        ('animals', '0002_initial_data_insertion')
    ]

    operations = [
        migrations.RunPython(insert_buildings, migrations.RunPython.noop),
        migrations.RunPython(insert_rooms, migrations.RunPython.noop),
        migrations.RunPython(insert_locations, migrations.RunPython.noop)
    ]