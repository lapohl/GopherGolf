# Generated by Django 3.2.2 on 2021-07-29 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0006_auto_20210611_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='area',
        ),
        migrations.AlterField(
            model_name='task',
            name='next_due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
