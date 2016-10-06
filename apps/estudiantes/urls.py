from django.conf.urls import url
from apps.estudiantes.views import *


urlpatterns=[
     url(r'^$', inicio),
]