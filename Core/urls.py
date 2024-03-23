from django.urls import path

from DiabEats import settings
from . import views
from .views import *
from .views import index
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
    path('signup/', signup_post, name='signup')
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)