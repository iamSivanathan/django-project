# Generated by Django 5.1.6 on 2025-03-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_bengaluruteamplayers_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='chennaiteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='chen_pl/'),
        ),
        migrations.AddField(
            model_name='eastbengalteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='goateamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='hyderabadteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='jamshedpurteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='keralateamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='mohammedanteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='mohunbaganteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='mumbaiteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='northeastteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='odishateamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
        migrations.AddField(
            model_name='punjabteamplayers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='beng_pl/'),
        ),
    ]
