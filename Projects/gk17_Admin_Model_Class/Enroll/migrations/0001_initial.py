# Generated by Django 4.2.4 on 2023-08-20 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=30)),
                ('Reg_No', models.CharField(max_length=30, unique=True)),
                ('Email', models.EmailField(max_length=30)),
                ('Description', models.TextField(max_length=100)),
            ],
        ),
    ]