# Generated by Django 3.1.6 on 2021-03-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20210321_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(upload_to='photo/%Y/%M/%D/'),
        ),
    ]
