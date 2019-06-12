from django.conf.urls import include, url
from django.contrib import admin
from back_stage import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.index, name='index'),
]
