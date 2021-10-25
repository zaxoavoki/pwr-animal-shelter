# Generated by Django 3.2.8 on 2021-10-25 23:44

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
                ('number', models.IntegerField(verbose_name='Numer budynku')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Numer pokoju')),
                ('capacity', models.IntegerField(verbose_name='Ilość mieść')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.building')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_to', models.DateTimeField(null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.room')),
            ],
        ),
    ]
