# Generated by Django 3.1.7 on 2021-04-03 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='mail',
        ),
    ]