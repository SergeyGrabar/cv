from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import PhotoProfile, PhotoDiploma, Contact, DiplomaDescription, Experience, Education, Language, Skills

@admin.register(PhotoProfile)
class PhotoProfileAdmin(TranslationAdmin):
    list_display = ['name','profile_image', 'info']
    list_editable = ['profile_image', 'info']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','number_vodafone','number_kyivstar','email', 'linkedin', 'telegram', 'github']
    list_editable = ['number_vodafone', 'number_kyivstar', 'email', 'linkedin', 'telegram', 'github']

@admin.register(PhotoDiploma)
class PhotoDiplomaAdmin(TranslationAdmin):
    list_display = ['id','title','diploma_image']
    list_editable = ['title','diploma_image']

@admin.register(DiplomaDescription)
class DiplomaDescriptionAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'photo_diploma']
    list_editable = ['title', 'photo_diploma']

@admin.register(Experience)
class ExperienceAdmin(TranslationAdmin):
    list_display = ['title', 'year_work', 'company_name', 'position', 'responsibilities']
    list_editable = ['year_work', 'company_name', 'position', 'responsibilities']
    ordering = ['-id']

@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    list_display = ['academy_name', 'city_name', 'profession', 'years_education']
    list_editable = ['city_name', 'profession', 'years_education']

@admin.register(Language)
class LanguageAdmin(TranslationAdmin):
    list_display = ['id', 'name_language', 'icon']
    list_editable = ['name_language', 'icon']

@admin.register(Skills)
class SkillsAdmin(TranslationAdmin):
    list_display = ['id', 'skill', 'progress', 'language']
    list_editable = ['skill', 'progress', 'language']