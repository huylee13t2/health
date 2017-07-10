from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.views import logout,login
from account import  views
urlpatterns = [
    url(r'^login/$', login, {'template_name':'account/login.html',}, name='login'),
    url(r'^logout/$',logout, {'next_page': reverse_lazy('frontend:homepage')}, name='logout'),
    url(r'^signup/$',views.user_registration, name='signup'),
    url(r'^profile/$', views.choose_profile, name='choose_profile' ),

]