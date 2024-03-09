# Generated by Django 4.2.4 on 2023-08-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30, unique=True)),
                ('Password', models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]