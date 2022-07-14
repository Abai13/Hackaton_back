from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CommentViewSet, ImageView, BrandViewSet, SneakersTypeViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('comments', CommentViewSet)
router.register('image', ImageView)
router.register('brand', BrandViewSet)
router.register('sneakers_type', SneakersTypeViewSet)

urlpatterns = []
urlpatterns += router.urls