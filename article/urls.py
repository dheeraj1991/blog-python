from django.conf.urls import patterns, include, url
from .views import ArticleList, ArticleDetail


urlpatterns = patterns('',
    url(r'^(?P<article_id>[0-9]+)', ArticleDetail.as_view()),
    url(r'^$', ArticleList.as_view()),
)

