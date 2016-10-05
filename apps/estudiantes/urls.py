from django.conf.urls import url
from .view import inicio
urlpatterns=[
     url(r'^$',' inicio', name='inicio'),
]