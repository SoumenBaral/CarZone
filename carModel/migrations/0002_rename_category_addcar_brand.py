# Generated by Django 4.2.7 on 2023-12-18 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carModel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcar',
            old_name='category',
            new_name='brand',
        ),
    ]
