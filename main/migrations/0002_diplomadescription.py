# Generated by Django 4.2.6 on 2023-10-17 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiplomaDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('photo_diploma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.photodiploma')),
            ],
        ),
    ]
