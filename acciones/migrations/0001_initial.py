# Generated by Django 4.1.3 on 2022-12-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
