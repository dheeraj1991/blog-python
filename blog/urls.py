from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from article.views import RandomContent


urlpatterns = patterns('',
    # URL pattern to access urls provided in article app
    url(r'^articles/', include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^random/', RandomContent.as_view()),
)

# Media URL to be served from /media/
urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
]