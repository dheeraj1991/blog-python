from django.db import models
import datetime


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    author = models.CharField(max_length=25,  verbose_name='Author')
    publication_date = models.DateField(verbose_name='Publication Date')
    hero_image = models.ImageField(
        default=datetime.date.today, verbose_name='Hero Image')
    optional_image = models.ImageField(
        blank=True, verbose_name='Alternate Image')
    content = models.TextField(verbose_name='Content')

    class Meta:
        app_label = 'article'
        db_table = 'blog_article'

    def __str__(self):
        return self.title
