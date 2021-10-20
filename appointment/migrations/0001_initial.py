# Generated by Django 3.2.8 on 2021-10-20 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_speciality', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time_slot', models.CharField(choices=[('1', '9:00 to 9:45'), ('2', '9:45 to 10:30'), ('3', '10:30 to 11:15'), ('4', '11:15 to 12:00'), ('5', '2:00 to 2:45'), ('6', '2:45 to 3:30'), ('7', '3:30 to 4:15'), ('8', '4:15 to 5:00')], max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_doctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
