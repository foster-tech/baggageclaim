from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView
from profiles.views import ProfileView, register
from claims.views import ClaimView, Claim1View, Claim2View, Claim3View, Claim4View
from app.views import DestinationView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'concept/', TemplateView.as_view(template_name='concept.html'), name='concept'),
    url(r'profile/', ProfileView, name='profile'),
    url(r'destination/', DestinationView, name='destination'),
    url(r'coming_soon/',TemplateView.as_view(template_name='coming_soon.html'), name='coming_soon'),

    url(r'claim/', ClaimView, name='claim'),
    url(r'claim1/', Claim1View, name='claim1'),
    url(r'claim2/', Claim2View, name='claim2'),
    url(r'claim3/', Claim3View, name='claim3'),
    url(r'claim4/', Claim4View, name='claim4'),
    url(r'preview/',TemplateView.as_view(template_name='preview.html'),name='preview'),
        
    url(r'press/', TemplateView.as_view(template_name='press.html'), name='press'),
    url(r'contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),

    path('accounts/register', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
