# Generated by Django 4.2.6 on 2023-11-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_language_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='progress',
            field=models.IntegerField(default=0, verbose_name='Прогрес'),
        ),
    ]
