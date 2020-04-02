# Generated by Django 3.0.4 on 2020-04-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20200330_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Role',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
