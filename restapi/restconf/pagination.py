from rest_framework.pagination import PageNumberPagination

class RestApiAppPagination(PageNumberPagination):
    page_size = 3