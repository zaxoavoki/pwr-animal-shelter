# Generated by Django 3.2.8 on 2021-12-01 22:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Ulica')),
                ('number', models.PositiveIntegerField(verbose_name='Numer budynku')),
            ],
            options={
                'verbose_name': 'Budynek',
                'verbose_name_plural': 'Budynki',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Numer pokoju')),
                ('capacity', models.PositiveIntegerField(verbose_name='Ilość miejsc')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='locations.building')),
            ],
            options={
                'verbose_name': 'Pokój',
                'verbose_name_plural': 'Pokoje',
            },
        ),
        migrations.CreateModel(
            name='AnimalLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data od')),
                ('date_to', models.DateTimeField(blank=True, null=True, verbose_name='Data do')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal', verbose_name='Zwierzę')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.room', verbose_name='Pokój')),
            ],
            options={
                'verbose_name': 'Lokalizacja Zwierzęcia',
                'verbose_name_plural': 'Lokalizacje Zwierząt',
            },
        ),
    ]
