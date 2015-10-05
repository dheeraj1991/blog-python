from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class ArticlesListPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'total_pages': self.page.paginator.num_pages,
                'current_page': self.page.number,
                'per_page': self.page.paginator.per_page,
                'page_range': self.page.paginator.page_range,
            },
            'articles': data
        })