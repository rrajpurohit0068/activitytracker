# Generated by Django 3.2.23 on 2023-12-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20231228_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
