# Generated by Django 4.1.3 on 2022-12-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos',
            name='pactivo',
            field=models.BooleanField(default=True),
        ),
    ]
