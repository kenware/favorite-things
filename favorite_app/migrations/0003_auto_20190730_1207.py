# Generated by Django 2.2.3 on 2019-07-30 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_app', '0002_auto_20190728_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='category',
            name='modified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]