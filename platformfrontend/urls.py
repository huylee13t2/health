from django.conf.urls import include, url
from platformfrontend import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    ]