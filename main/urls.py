from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.About.as_view(), name='about'),
    path('experience/', views.Experience.as_view(), name='experience'),
    path('education/', views.Education.as_view(), name='education'),
    path('certificates/', views.CertificatesViews.as_view(), name='certificates'),
    path('certificates/<int:pk>', views.CertificatesDetailView.as_view(), name='detail'),
    path('skills/', views.LanguageView.as_view(), name='skills'),
    path('contacts/', views.MyContacts.as_view(), name='contacts'),
    path("set_language/<str:language>", views.set_language, name="set-language"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)