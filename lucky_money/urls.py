"""lucky_money URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lucky_money import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^$', views.home, name='home'),
url(r'^(?P<pk>\d+)/quota/$', views.quota, name='quota'),
url(r'^quota//(?P<pk>\d+)/receive$', views.receive, name='receive'),
url(r'^generate$', views.generate, name='generate'),
url(r'^generate_one/(?P<pk>\d+)/$', views.generate_one, name='generate_one'),
url(r'^generate_all/(?P<pk>\d+)/$', views.generate_all, name='generate_all'),
]
