# Generated by Django 3.2.2 on 2021-06-04 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-01-01'),
        ),
    ]
