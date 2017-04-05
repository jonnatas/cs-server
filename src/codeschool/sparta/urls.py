from django.conf.urls import url

from codeschool.sparta.views import hello_view


urlpatterns = [
    url(r'^hello/$', hello_view, name='hello'),
]


