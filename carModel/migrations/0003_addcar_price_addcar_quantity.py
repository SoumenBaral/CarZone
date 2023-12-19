# Generated by Django 4.2.7 on 2023-12-18 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carModel', '0002_rename_category_addcar_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcar',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='addcar',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]