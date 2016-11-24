from django.conf.urls import url
from bingo.views import *

urlpatterns = [
    url(r'^$', bingo, name='bingo'),
    url(r'^toggle/?$', toggle, name='toggle'),
    url(r'^reset/?$', reset, name='reset'),
]
