# Generated by Django 4.0.3 on 2022-04-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task',
            field=models.CharField(default='task1', max_length=200),
        ),
    ]