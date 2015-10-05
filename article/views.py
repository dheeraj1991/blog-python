from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.decorators import renderer_classes
from .serializers import ArticleSerializer
from .paginator import ArticlesListPagination
from .models import Article
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ArticleList(generics.ListAPIView):

    """
        List all articles and remove the once which have published date greater than today.
    """
    permission_classes = (IsAuthenticatedOrReadOnly, )
    renderer_classes = (JSONRenderer, )
    serializer_class = ArticleSerializer
    pagination_class = ArticlesListPagination
    paginate_by = 10
    raise_exception = True

    def get_queryset(self):
        return Article.objects.filter(publication_date__lt=datetime.date.today() + datetime.timedelta(days=1)).order_by('publication_date')


class ArticleDetail(APIView):
    """
        Details of a single article based on its id 
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
            serializer = ArticleSerializer(article)
            return Response({'article': serializer.data}, status.HTTP_200_OK)
        except:
            return Response({'error': 'Article with that ID does not exist'})