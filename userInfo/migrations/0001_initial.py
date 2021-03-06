# Generated by Django 4.0.4 on 2022-05-12 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('MR', 'MR'), ('Mrs', 'Mrs'), ('Chief', 'Chief'), ('Dr', 'Dr'), ('Engr', 'Engr'), ('senator', 'Senator'), ('Arch', 'Arch'), ('Bar', 'Barr')], max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('x_reservation', models.BooleanField(null=True)),
                ('discount_code', models.CharField(blank=True, max_length=200)),
                ('check_in', models.CharField(max_length=200)),
                ('check_out', models.CharField(max_length=200)),
                ('payment_status', models.BooleanField()),
                ('confirm_user_lodge', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
