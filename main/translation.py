from modeltranslation.translator import register, TranslationOptions
from .models import PhotoProfile, DiplomaDescription, PhotoDiploma, Experience, Education, Language, Skills

@register(PhotoProfile)
class PhotoProfileTranslationOptions(TranslationOptions):
    fields = ('info',)

@register(DiplomaDescription)
class DiplomaDescriptionTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(PhotoDiploma)
class PhotoDiplomaTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('title', 'company_name', 'position', 'responsibilities')

@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('academy_name', 'city_name', 'profession')

@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('name_language',)

@register(Skills)
class SkillsTranslationOptions(TranslationOptions):
    fields = ('skill',)