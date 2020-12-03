from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='cont.html'), name='cont'),
    path('start', TemplateView.as_view(template_name='start.html'), name='start'),
    path('start2', TemplateView.as_view(template_name='start2.html'), name='start2'),
    path('admin/', admin.site.urls),
    path('KnightEats/', include('django.contrib.auth.urls')),
    path('AccountManagement/', include('AccountManagement.urls')),
    path('OrderingSystem/', include('OrderingSystem.urls')),
    path('homepage/', include('homepage.urls')),
]
