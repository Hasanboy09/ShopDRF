from django.test import TestCase

from apps.models import Category
from apps.serializers import CategoryModelSerializer


class TestCategorySerializer(TestCase):
    def setUp(self):
        Category.objects.create(name='Texnika')
        Category.objects.create(name='Uy jihozlari')

    def test_serializer(self):  # obj > json
        obj = Category.objects.get(name='Texnika')
        data = CategoryModelSerializer(obj).data  # jsonga o`tish joyi # noqa
        assert isinstance(data, dict)
        assert data['name'] == 'Texnika'
        assert data['id'] == 1

    def test_deserializer(self):  # dict> obj
       data = {"name": "Telefon"}
       obj = CategoryModelSerializer(data=data)
       assert obj.is_valid()
       assert obj.validated_data['name'] == 'Telefon'
