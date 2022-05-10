# Generated by Django 4.0.4 on 2022-05-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=500)),
                ('room_description', models.CharField(max_length=1000)),
                ('room_price', models.CharField(max_length=50)),
                ('roomImage', models.ImageField(upload_to=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]
