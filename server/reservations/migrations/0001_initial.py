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
            name='ReservationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, unique=True, verbose_name='Wartość')),
            ],
            options={
                'verbose_name': 'Status Rezerwacji',
                'verbose_name_plural': 'Statusy Rezerwacji',
            },
        ),
        migrations.CreateModel(
            name='AnimalReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.animal', verbose_name='Zwierzę')),
                ('reservation_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations.reservationstatus', verbose_name='Status Rezerwacji')),
            ],
            options={
                'verbose_name': 'Rezerwacja Zwierzęica',
                'verbose_name_plural': 'Rezerwacje Zwierząt',
            },
        ),
    ]
