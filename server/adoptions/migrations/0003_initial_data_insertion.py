# Generated by Django 3.2.8 on 2021-11-08 11:07

from django.db import migrations


def insert_adoptions(apps, schema_editor):
    AnimalAdoption = apps.get_model('adoptions', 'AnimalAdoption')
    User = apps.get_model('users', 'User')
    Animal = apps.get_model('animals', 'Animal')

    for _ in range(35):
        user = User.objects.order_by('?').first()
        animal = Animal.objects.order_by('?').first()
        AnimalAdoption.objects.create(user=user, animal=animal)



class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_animaladoption_user'),
        ('users', '0002_initial_data_insertion')
    ]

    operations = [
        migrations.RunPython(insert_adoptions, migrations.RunPython.noop)
    ]
