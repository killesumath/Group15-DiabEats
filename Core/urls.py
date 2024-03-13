from django.urls import path

from DiabEats import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)