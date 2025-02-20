# Generated by Django 5.1.2 on 2024-11-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('agree', models.BooleanField()),
                ('BirthDate', models.DateField()),
                ('birth_year', models.DateField()),
                ('fav_color', models.CharField(max_length=100)),
                ('fav_color1', models.CharField(max_length=100)),
            ],
        ),
    ]
