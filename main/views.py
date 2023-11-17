from typing import Any
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.utils.translation import gettext as _
from .models import Contact, PhotoProfile, PhotoDiploma, DiplomaDescription, Experience, Education, Language, Skills
from .forms import ContactForm
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from django.contrib import messages
from django.core.exceptions import ValidationError

def index(reqest):
    return render(reqest, 'index.html', {'title': _('Головна')})

class About(ListView):
    '''
    Про мене
    '''
    model = PhotoProfile
    template_name = 'about.html'
    context_object_name = 'contents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Про мене')

        return context

class Experience(ListView):
    '''
    Досвід роботи
    '''
    model = Experience
    template_name = 'experience.html'
    context_object_name = 'works'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Досвід роботи')

        return context

class Education(ListView):
    '''
    Освіта
    '''
    model = Education
    template_name = 'education.html'
    context_object_name = 'educations'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Освіта')

        return context

class CertificatesViews(ListView):
    '''Відображення дипломів'''
    model = PhotoDiploma
    template_name = 'certificates.html'
    context_object_name = 'diplomas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Дипломи')
        return context

class CertificatesDetailView(DetailView):
    model = PhotoDiploma
    template_name = 'certificates_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['descriptions'] = DiplomaDescription.objects.filter(photo_diploma=self.object)
        context['title'] = _('Пройдений матеріал')
        return context

class LanguageView(ListView):
    '''Навички'''
    model = Language
    template_name = 'skills.html'
    context_object_name = 'languages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Навички')

        return context

class MyContacts(TemplateView):
    template_name = 'contacts.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Контакти')
        context['contents'] = Contact.objects.all()
        context['form'] = ContactForm()

        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].title()
            email = form.cleaned_data['email']
            message = f"Ім'я: {name}\nEmail: {email}\nПовідомлення: {form.cleaned_data['message']}"
            mail = send_mail(form.cleaned_data['subject_message'], message, 'sergeygrabar@gmail.com', ['serhiihrabar@ukr.net'], fail_silently=True)
            if mail:
                messages.success(request, _('Повідомлення надіслане'))
                send_mail('Дякую за відгук!!!', f'Дякую за відгук {name}. Я ціную вашу думку!', 'sergeygrabar@gmail.com', [f'{email}'])
                return redirect('contacts')
            else:
                messages.error(request, _('Помилка відправки'))
                return redirect('contacts')
        else:
            messages.error(request, _('Введено не коректний email'))
            return redirect('contacts')
                

#=====================================
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response