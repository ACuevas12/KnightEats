from django.urls import path, include
from homepage.views import HomepageDefaultView1, index
from . import views

urlpatterns = [
    path('1/', HomepageDefaultView1.as_view(), name='view1'),
    path('empty/', views.index, name='placeholder')
]
