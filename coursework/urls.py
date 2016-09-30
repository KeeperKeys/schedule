from django.conf.urls import patterns, include, url
from django.contrib import admin

# admin.autodiscover()

urlpatterns = patterns('timetable',
                       # Examples:
                       # url(r'^$', 'coursework.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'views.main_page'),
                       url(r'^dantzig/$', 'algorithms.views.dantzig'),
                       url(r'^dantzig/matrix/$', 'algorithms.views.dantzig_matrix'),
                       url(r'^groups/$', 'views.groups'),
                       url(r'^groups/(\w+-\w+)/$', 'views.selected_group'),
                       url(r'^groups/(\w+-\w+)/pdf$', 'views.selected_group_pdf'),
                       # url(r'groups/(\w+-\w+)/(\w+)/(\d+)/(\w+)/$', 'views.selected_lesson'),
                       url(r'^groups/(\w+-\w+)/(\d+)/(\d+)/(\w+)/$', 'views.selected_lesson'),
                       url(r'^teachers/xml/$', 'views.teachers_xml'),
                       url(r'accounts/login/$', 'users.views.login'),
                       url(r'accounts/logout/$', 'users.views.logout'),
                       url(r'accounts/loggedin/$', 'users.views.loggedin'),
                       url(r'accounts/loggedout/$', 'users.views.loggedout'),
                       )
