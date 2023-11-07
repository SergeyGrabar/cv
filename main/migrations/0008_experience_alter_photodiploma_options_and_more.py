# Generated by Django 4.2.6 on 2023-10-24 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_photoprofile_options_alter_photoprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Досвід роботи')),
                ('title_uk', models.CharField(max_length=20, null=True, verbose_name='Досвід роботи')),
                ('title_en', models.CharField(max_length=20, null=True, verbose_name='Досвід роботи')),
                ('year_work', models.CharField(max_length=20, verbose_name='Роки роботи')),
                ('company_name', models.CharField(max_length=20, verbose_name='Назва компанії')),
                ('company_name_uk', models.CharField(max_length=20, null=True, verbose_name='Назва компанії')),
                ('company_name_en', models.CharField(max_length=20, null=True, verbose_name='Назва компанії')),
                ('position', models.CharField(max_length=20, verbose_name='Посада')),
                ('position_uk', models.CharField(max_length=20, null=True, verbose_name='Посада')),
                ('position_en', models.CharField(max_length=20, null=True, verbose_name='Посада')),
                ('responsibilities', models.TextField(verbose_name="Обов'язки")),
                ('responsibilities_uk', models.TextField(null=True, verbose_name="Обов'язки")),
                ('responsibilities_en', models.TextField(null=True, verbose_name="Обов'язки")),
            ],
            options={
                'verbose_name': 'Досвід роботи',
            },
        ),
        migrations.AlterModelOptions(
            name='photodiploma',
            options={'verbose_name_plural': 'Дипломи'},
        ),
        migrations.AlterModelOptions(
            name='photoprofile',
            options={'verbose_name': 'Данні профіля', 'verbose_name_plural': 'Про мене'},
        ),
        migrations.AlterField(
            model_name='diplomadescription',
            name='photo_diploma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.photodiploma', verbose_name='Назва Академії'),
        ),
        migrations.AlterField(
            model_name='diplomadescription',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='diplomadescription',
            name='title_en',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='diplomadescription',
            name='title_uk',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='photodiploma',
            name='diploma_image',
            field=models.ImageField(upload_to='photo_diploma/', verbose_name='Фото диплому'),
        ),
        migrations.AlterField(
            model_name='photodiploma',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Назва Академії'),
        ),
        migrations.AlterField(
            model_name='photodiploma',
            name='title_en',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Назва Академії'),
        ),
        migrations.AlterField(
            model_name='photodiploma',
            name='title_uk',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='Назва Академії'),
        ),
        migrations.AlterField(
            model_name='photoprofile',
            name='info',
            field=models.TextField(default='', verbose_name='Інформація'),
        ),
        migrations.AlterField(
            model_name='photoprofile',
            name='info_en',
            field=models.TextField(default='', null=True, verbose_name='Інформація'),
        ),
        migrations.AlterField(
            model_name='photoprofile',
            name='info_uk',
            field=models.TextField(default='', null=True, verbose_name='Інформація'),
        ),
        migrations.AlterField(
            model_name='photoprofile',
            name='name',
            field=models.CharField(default='Данні профіля', max_length=20, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='photoprofile',
            name='profile_image',
            field=models.ImageField(upload_to='photo_profile/', verbose_name='Фото профіля'),
        ),
    ]
