# Generated by Django 5.1.6 on 2025-03-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_remove_teamstanding_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamstanding',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='club_img/'),
        ),
    ]
