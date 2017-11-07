from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^character/create', views.create_character, name='create'),
    url(r'^character/index', views.index, name='index'),
]