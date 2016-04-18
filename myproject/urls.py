from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^annotated/insert/$', 'cms_templates.views.annotated'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^annotated/pages/$', "cms.views.showPages"),
    url(r'^(\d+)$', "cms.views.page"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$', 'cms_templates.views.redirect'),
    url(r'.*', "cms.views.notFound")
)
