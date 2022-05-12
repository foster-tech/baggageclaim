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
    path('^$', TemplateView.as_view(template_name='home.html'), name='home'),
    path('concept/', TemplateView.as_view(template_name='concept.html'), name='concept'),
    path('profile/', ProfileView, name='profile'),
    path('destination/', DestinationView, name='destination'),
    path('coming_soon/',TemplateView.as_view(template_name='coming_soon.html'), name='coming_soon'),

    path('claim/', ClaimView, name='claim'),
    path('claim1/', Claim1View, name='claim1'),
    path('claim2/', Claim2View, name='claim2'),
    path('claim3/', Claim3View, name='claim3'),
    path('claim4/', Claim4View, name='claim4'),
    path('preview/',TemplateView.as_view(template_name='preview.html'),name='preview'),
        
    path('press/', TemplateView.as_view(template_name='press.html'), name='press'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('privacy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),

    path('accounts/register', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
