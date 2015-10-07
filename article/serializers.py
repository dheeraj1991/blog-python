from rest_framework import serializers
from django.conf import settings
from datetime import datetime

from .models import Article
import logging

logger = logging.getLogger(__name__)


class ArticleSerializer(serializers.Serializer):

    class Meta:
        model = Article

    def to_representation(self, obj):
        try:
            if obj.optional_image and not self.context.get('random'):
                optional_image = settings.BASE_URL + obj.optional_image.url
            else:
                optional_image = None
            return {
                'id': obj.id,
                'title': obj.title,
                'author': obj.author,
                'publication_date': datetime.strftime(obj.publication_date, "%A, %B %d, %Y"),
                'hero_image': settings.BASE_URL + obj.hero_image.url,
                'optional_image': optional_image,
                'content': obj.content,
            }
        except Exception as e:
            print e