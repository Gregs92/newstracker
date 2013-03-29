from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.defaults import handler404, handler500

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'tracker.views.index'),
	url(r'^analysis/', 'tracker.views.analysis'),
	url(r'^about/', 'tracker.views.about')
    # url(r'^newstracker/', include('newstracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
)
 
handler500 = 'tracker.views.error_500'
handler404 = 'tracker.views.error_404'


#testing 404 and 500 pages
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^404/$', 'django.views.defaults.page_not_found'),
        	(r'^500/$', 'django.views.defaults.server_error'),
	)