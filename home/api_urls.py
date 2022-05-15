from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import ProductViewSet, ProductFilterView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('product_filter', ProductFilterView.as_view(), name='product_filter'),
]
