#from django.conf.urls import patterns, include, url
#from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from . import views
from . import memberform

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('member/', memberform.member, name='member'),
]
#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tsap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
#)
