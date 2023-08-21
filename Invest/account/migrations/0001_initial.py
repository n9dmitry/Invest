# Generated by Django 4.2.4 on 2023-08-10 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_info', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('phone_verified', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
                ('favorites', models.ManyToManyField(to='item.item')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
