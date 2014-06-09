from django.conf.urls import patterns, include, url

from django.contrib import admin
from core.views import JobList, JobDetail

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emplea_do.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', JobList.as_view()),
    url(r'^job/(?P<pk>\d+)/$', JobDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
