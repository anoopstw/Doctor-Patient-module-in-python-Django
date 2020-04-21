# Generated by Django 3.0.4 on 2020-04-03 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_doctor_department'),
        ('search', '0003_patient_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]