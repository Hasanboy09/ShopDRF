from django.test import TestCase

from apps.models import Category


class TestCategoryView(TestCase):
    def setUp(self):
        Category.objects.create(name='Texnika')
        Category.objects.create(name='Uy jihozlari')

    def test_get_list(self):
        obj = Category.objects.all()
        self.assertEqual(len(obj), 2)

    def test_get(self):
        obj = Category.objects.all()
        assert obj[0].name == 'Texnika'



