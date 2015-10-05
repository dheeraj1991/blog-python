from django.contrib import admin
from .models import Article
from django.contrib.auth.models import Group


admin.site.register(Article)
admin.site.unregister(Group)