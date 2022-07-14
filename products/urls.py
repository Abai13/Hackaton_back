from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CommentViewSet, ImageView, BrandViewSet, CategoryViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('comments', CommentViewSet)
router.register('image', ImageView)
router.register('brand', BrandViewSet)
router.register('category', CategoryViewSet)

urlpatterns = []
urlpatterns += router.urls