# Generated by Django 4.0.3 on 2022-03-20 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0002_electronic_species'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electronic',
            name='species',
        ),
    ]
