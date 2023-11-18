# Generated by Django 4.2.6 on 2023-10-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_experience_options_contact_github_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academy_name', models.CharField(max_length=50, verbose_name='Назва Академії')),
                ('city_name', models.CharField(max_length=50, verbose_name='Місто')),
                ('years_education', models.CharField(max_length=50, verbose_name='Роки навчання')),
                ('profession', models.CharField(max_length=50, verbose_name='Професія')),
            ],
            options={
                'verbose_name_plural': 'Освіта',
            },
        ),
    ]