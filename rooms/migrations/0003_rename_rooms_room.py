# Generated by Django 4.0.4 on 2022-05-12 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_rooms_created_at_alter_rooms_roomimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
    ]
