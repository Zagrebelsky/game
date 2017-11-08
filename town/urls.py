from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^town/town', views.town, name='town'),
]