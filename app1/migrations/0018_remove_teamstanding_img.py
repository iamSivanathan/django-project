# Generated by Django 5.1.6 on 2025-03-11 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_teamstanding_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamstanding',
            name='img',
        ),
    ]
