# Generated by Django 4.0.3 on 2022-03-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_swimwear_bustsize_swimwear_hipssize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dress',
            name='lenght',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dress',
            name='pattern',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dress',
            name='size',
            field=models.CharField(max_length=255),
        ),
    ]
