# Generated by Django 5.0 on 2023-12-24 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(null=True, upload_to='media/core'),
        ),
    ]
