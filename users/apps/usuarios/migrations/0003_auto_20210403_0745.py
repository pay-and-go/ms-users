# Generated by Django 3.1.7 on 2021-04-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_usuario_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='mail',
            field=models.EmailField(default='DEFAULT VALUE', max_length=254),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
