# Generated by Django 5.1.6 on 2025-03-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_mohunbaganteamplayers_mumbaiteamplayers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamstanding',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='club_img/'),
        ),
    ]
