from rest_framework import serializers

from .models import Article
import logging

logger = logging.getLogger(__name__)


class ArticleSerializer(serializers.Serializer):

    class Meta:
        model = Article

    def to_representation(self, obj):
        try:
            print obj.optional_image
            if obj.optional_image:
                optional_image = obj.optional_image.url
            else:
                optional_image = ""
            return {
                'id': obj.id,
                'title': obj.title,
                'author': obj.author,
                'publication_date': obj.publication_date,
                'hero_image': obj.hero_image.url,
                'optional_image': optional_image,
                'content': obj.content
            }
        except Exception as e:
            print e