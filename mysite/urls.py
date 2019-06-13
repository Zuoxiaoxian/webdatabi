from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^backstage/$', include('back_stage.urls', namespace='backstage')),
    
    url(r'', include('back_stage.urls', namespace='backstage')),
    url(r'^admin/', include(admin.site.urls)),

]
