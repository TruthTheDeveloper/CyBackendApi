# Generated by Django 4.0.4 on 2022-05-18 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userInfo', '0002_alter_userinfo_first_name_alter_userinfo_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ('created_at',)},
        ),
    ]
