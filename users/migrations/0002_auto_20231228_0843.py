# Generated by Django 3.2.23 on 2023-12-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.TextField(blank=True, default=''),
        ),
    ]
