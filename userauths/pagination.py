from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100 
    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get('disable_pagination', 'false').lower() == 'true':
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        if self.page is None:
            return Response(data)
        return super().get_paginated_response(data)