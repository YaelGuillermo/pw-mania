# Generated by Django 4.1.13 on 2023-11-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_album_image_alter_artist_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='nationality',
        ),
        migrations.AddField(
            model_name='country',
            name='image',
            field=models.ImageField(null=True, upload_to='countries'),
        ),
    ]