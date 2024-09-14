from rest_framework.generics import ListCreateAPIView

from apps.models import Category
from apps.serializers import CategoryModelSerializer



class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer