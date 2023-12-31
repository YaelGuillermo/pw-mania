# Generated by Django 4.2.7 on 2023-11-29 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='nationality',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.country'),
        ),
    ]
