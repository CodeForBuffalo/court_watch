"""courtwatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from courtwatchsite	import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # /stories/
    url(r'^stories/$', views.stories, name='stories'),
    url(r'^stories/(?P<pk>\d+)/$', views.next, name='next'),
    # /statistics/
    url(r'^statistics/$', views.statistics, name='statistics'),
    # /resources/
    url(r'^resources/$', views.resources, name='resources'),
    # /join/
    url(r'^join/$', views.join, name='join'),
    # /contact/
    url(r'^contact/$', views.contact, name='contact'),
    # /login/
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),  
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"), 
    url(r'^member/$', views.member, name='member'),       
    url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
