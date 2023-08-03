# Generated by Django 4.2.4 on 2023-08-02 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('city', models.CharField(max_length=255)),
                ('required_investment', models.CharField(max_length=255)),
                ('profit_per_month', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('item_id', models.IntegerField()),
                ('parent_category_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemStatistics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('count_view', models.IntegerField()),
                ('count_phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFavoriteItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='A',
        ),
    ]
