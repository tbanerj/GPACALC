# Generated by Django 5.0.1 on 2024-01-29 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpaCalc', '0005_class_lettergrade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='grade',
        ),
    ]