# Generated by Django 4.2.6 on 2023-10-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_diplomadescription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Контакти'},
        ),
        migrations.AlterModelOptions(
            name='diplomadescription',
            options={'verbose_name': 'Опис дипломів', 'verbose_name_plural': 'Описи дипломів'},
        ),
        migrations.AlterModelOptions(
            name='photodiploma',
            options={'verbose_name_plural': 'Фото дипломів'},
        ),
        migrations.AlterModelOptions(
            name='photoprofile',
            options={'verbose_name_plural': 'Фото профіля'},
        ),
        migrations.AddField(
            model_name='photoprofile',
            name='info',
            field=models.TextField(default=''),
        ),
    ]