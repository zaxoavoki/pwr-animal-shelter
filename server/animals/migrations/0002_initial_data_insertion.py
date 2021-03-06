# Generated by Django 3.2.8 on 2021-11-07 13:40

from django.db import migrations
from faker import Faker
from faker.providers import color, lorem, person, python

fake = Faker()
fake.add_provider(color)
fake.add_provider(lorem)
fake.add_provider(person)
fake.add_provider(python)


def insert_genders(apps, schema_editor):
    genders = ['Samiec', 'Samica', 'Nie wiadomo']
    AnimalGender = apps.get_model('animals', 'AnimalGender')
    for gender in genders:
        AnimalGender.objects.create(value=gender)


def insert_statuses(apps, schema_editor):
    statuses = ['Gotowe do adopcji', 'Kwarantanna', 'Zaadoptowane', 'Zarezerwowane', 'Nie żyje']
    AnimalStatus = apps.get_model('animals', 'AnimalStatus')
    for status in statuses:
        AnimalStatus.objects.create(value=status)


def insert_types(apps, schema_editor):
    types = ['Pies', 'Kot', 'Świnia', 'Królik']
    AnimalType = apps.get_model('animals', 'AnimalType')
    for type_ in types:
        AnimalType.objects.create(value=type_)


def insert_breeds(apps, schema_editor):
    breeds = ['Chihuahua', 'Niemiecki owczarek', 'Buldog', 'Mieszaniec']
    AnimalBreed = apps.get_model('animals', 'AnimalBreed')
    for breed in breeds:
        AnimalBreed.objects.create(value=breed)


def get_random(model):
    return model.objects.order_by("?").first()


def insert_animals(apps, schema_editor):
    Animal = apps.get_model('animals', 'Animal')
    AnimalBreed = apps.get_model('animals', 'AnimalBreed')
    AnimalStatus = apps.get_model('animals', 'AnimalStatus')
    AnimalType = apps.get_model('animals', 'AnimalType')
    AnimalGender = apps.get_model('animals', 'AnimalGender')

    for _ in range(7):
        breed = get_random(AnimalBreed)
        status = AnimalStatus.objects.order_by("?").filter(value = 'Gotowe do adopcji').first()
        type_ = get_random(AnimalType)
        gender = get_random(AnimalGender)

        height = fake.pyint(min_value=20, max_value=200)
        weight = fake.pyint(min_value=20, max_value=200)
        age = fake.pyint(min_value=1, max_value=20)
        vaccinations = fake.paragraph(nb_sentences=1)
        color = fake.safe_color_name()
        name = fake.first_name_nonbinary()
        chip_code = fake.uuid4()
        description = fake.paragraph(nb_sentences=5)

        Animal.objects.create(age=age, color=color, weight=weight, chip_code=chip_code, description=description, height=height,
                              vaccinations=vaccinations, name=name, animal_breed=breed, animal_status=status, animal_gender=gender, animal_type=type_, )


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_genders, migrations.RunPython.noop),
        migrations.RunPython(insert_statuses, migrations.RunPython.noop),
        migrations.RunPython(insert_types, migrations.RunPython.noop),
        migrations.RunPython(insert_breeds, migrations.RunPython.noop),
        migrations.RunPython(insert_animals, migrations.RunPython.noop)
    ]