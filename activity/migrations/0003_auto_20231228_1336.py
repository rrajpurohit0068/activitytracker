# Generated by Django 3.2.23 on 2023-12-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20231228_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='background_color',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='status',
            name='text_color',
            field=models.TextField(blank=True, default=''),
        ),
    ]
