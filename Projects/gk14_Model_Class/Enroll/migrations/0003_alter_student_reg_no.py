# Generated by Django 4.2.4 on 2023-08-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enroll', '0002_alter_student_reg_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Reg_NO',
            field=models.IntegerField(max_length=30),
        ),
    ]
