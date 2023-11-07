from django.db import models

class PhotoProfile(models.Model):
    name = models.CharField(max_length=20, default='Данні профіля', verbose_name='Назва')
    profile_image = models.ImageField(upload_to='photo_profile/', verbose_name='Фото профіля')
    info = models.TextField(default='', verbose_name='Інформація')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Данні профіля'
        verbose_name_plural = "Про мене"

class PhotoDiploma(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Назва Академії')
    diploma_image = models.ImageField(upload_to='photo_diploma/', verbose_name='Фото диплому')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = "Дипломи"

class DiplomaDescription(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Назва')
    photo_diploma = models.ForeignKey(PhotoDiploma, on_delete=models.CASCADE, verbose_name='Назва Академії')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Опис дипломів"
        verbose_name_plural = "Описи дипломів"

class Contact(models.Model):
    number_vodafone = models.CharField(max_length=20, verbose_name='Водафон')
    number_kyivstar = models.CharField(max_length=20, verbose_name='Київстар')
    email = models.EmailField(verbose_name='E-mail')
    linkedin = models.URLField(verbose_name='LinkedIn')
    telegram = models.URLField(verbose_name='Telegram')
    github = models.URLField(verbose_name='GitHub', default='')

    def __str__(self):
        return f'Контакти'
    
    class Meta:
        verbose_name_plural = "Контакти"

class Experience(models.Model):
    title = models.CharField(max_length=50, verbose_name='Роботодавець')
    year_work = models.CharField(max_length=20, verbose_name='Роки роботи')
    company_name = models.CharField(max_length=50, verbose_name='Назва компанії')
    position = models.CharField(max_length=50, verbose_name='Посада')
    responsibilities = models.TextField(verbose_name="Обов'язки")

    def __str__(self):
        return f'{self.company_name}'
    
    class Meta:
        verbose_name_plural = 'Досвід роботи'

class Education(models.Model):
    academy_name = models.CharField(max_length=100, verbose_name='Назва Академії')
    city_name = models.CharField(max_length=50, verbose_name='Місто')
    years_education = models.CharField(max_length=50, verbose_name='Роки навчання')
    profession = models.CharField(max_length=50, verbose_name='Професія')

    def __str__(self):
        return f'{self.academy_name}'

    class Meta:
        verbose_name_plural = 'Освіта'

class Language(models.Model):
    name_language = models.CharField(max_length=100, verbose_name='Мова програмування')
    icon = models.TextField(verbose_name='Іконка', default='')

    def __str__(self):
        return f'{self.name_language}'

    class Meta:
        verbose_name_plural = 'Мова програмування'

class Skills(models.Model):
    skill = models.CharField(max_length=100, verbose_name='Навик')
    progress = models.IntegerField(verbose_name='Прогрес', default=0, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Мова програмування')

    def __str__(self):
        return f'{self.skill}'

    class Meta:
        verbose_name_plural = 'Навик'


