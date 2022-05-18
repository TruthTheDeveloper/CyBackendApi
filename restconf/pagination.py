from rest_framework import pagination

class CyBackendApiPagination(pagination.PageNumberPagination):
    page_size = 5