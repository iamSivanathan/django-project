# Generated by Django 5.1.6 on 2025-03-03 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_jersey_number_players_jersey_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Club', models.CharField(max_length=40)),
                ('form', models.CharField(max_length=5)),
            ],
        ),
    ]
