# Generated by Django 4.2.6 on 2023-10-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_language_alter_education_academy_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='icon',
            field=models.TextField(default='', verbose_name='Іконка'),
        ),
    ]