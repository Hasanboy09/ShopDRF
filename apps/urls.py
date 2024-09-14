from django.urls import path

from apps.views import CategoryListCreateAPIView

urlpatterns = [
    path('category', CategoryListCreateAPIView.as_view()),
]
