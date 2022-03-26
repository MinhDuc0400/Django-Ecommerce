# Generated by Django 4.0.3 on 2022-03-19 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('color', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clothes.clothes')),
                ('size', models.CharField(max_length=5)),
                ('lenght', models.CharField(max_length=5)),
                ('pattern', models.CharField(max_length=5)),
            ],
            bases=('clothes.clothes',),
        ),
        migrations.CreateModel(
            name='Jean',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clothes.clothes')),
                ('pipe', models.CharField(max_length=5)),
                ('size', models.CharField(max_length=5)),
            ],
            bases=('clothes.clothes',),
        ),
        migrations.CreateModel(
            name='SwimWear',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clothes.clothes')),
            ],
            bases=('clothes.clothes',),
        ),
        migrations.CreateModel(
            name='ClothesItem',
            fields=[
                ('barCode', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='clothes/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('clothes', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='clothes.clothes')),
            ],
        ),
    ]
