# Generated by Django 5.1.6 on 2025-03-03 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_standing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standing',
            old_name='Club',
            new_name='club',
        ),
    ]
