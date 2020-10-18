from django.conf.urls import include, url
from django.contrib.auth import logout
from . import views

app_name = 'accounts'

urlpatterns = [
        #User
        url(r'^login/$', views.login_view, name='login'),
        url(r'^logout/$', views.logout_view, name='logout'),
        url(r'^register/$', views.register_view, name='register'),
        url(r'^search/$', views.search_username, name='search'),
]
