# Generated by Django 5.1.5 on 2025-03-06 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_teamstanding_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='jersey_no',
        ),
        migrations.RemoveField(
            model_name='players',
            name='redcard',
        ),
        migrations.RemoveField(
            model_name='players',
            name='yellowcard',
        ),
    ]
