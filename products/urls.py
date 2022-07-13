from django.urls import path
from .views import ProductViewSet, CommentViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('comments', CommentViewSet)

urlpatterns = []
urlpatterns += router.urls # urlpatterns.extend(router.urls)