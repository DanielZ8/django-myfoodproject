# Generated by Django 4.1.7 on 2023-02-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_food_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='img',
            field=models.ImageField(blank=True, upload_to='food'),
        ),
    ]