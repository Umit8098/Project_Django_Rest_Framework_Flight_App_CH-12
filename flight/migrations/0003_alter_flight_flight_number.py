# Generated by Django 4.1.7 on 2025-01-09 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_alter_flight_flight_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=10),
        ),
    ]
