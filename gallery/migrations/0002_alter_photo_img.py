# Generated by Django 3.2.8 on 2021-10-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='artciles'),
        ),
    ]
