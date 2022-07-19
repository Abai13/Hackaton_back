from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CommentViewSet, BrandViewSet, CategoryViewSet, LikeViewSet # FavoritesViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, 'list')
router.register('comments', CommentViewSet)
# router.register('image', ImageView) # для загрузки большего кол-во изображений
router.register('brand', BrandViewSet)
router.register('category', CategoryViewSet)
# router.register('favorites', FavoritesViewSet)
router.register('likes', LikeViewSet)

urlpatterns = []
urlpatterns += router.urls