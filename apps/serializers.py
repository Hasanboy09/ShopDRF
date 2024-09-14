from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = 'slug',


    def validate(self, attrs):
        if len(attrs['name']) < 3:
            raise ValidationError({"name": "name must be at least 3 characters"})
        return attrs
