from django.conf.urls import url
from NewApp import views


urlpatterns=[
    url(r'^$',views.help ,name='help')
]
