# Generated by Django 4.0.3 on 2022-03-20 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='swimwear',
            name='bustSize',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='swimwear',
            name='hipsSize',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='swimwear',
            name='waistSize',
            field=models.IntegerField(default=0),
        ),
    ]
