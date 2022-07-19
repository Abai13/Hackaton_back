from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from accounts.admin import User
from products.filters import ProductPriceFilter
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 

from .models import Product, CommentRating, Category, Brand, Like, Favorites #Image
from .serializers import ProductSerializer, ReviewSerializer, BrandSerializer, CategorySerializer # LikeSerializer, FavoritesSerializer #ImageSerializer
from .permissions import IsAuthor

from products.filters import ProductPriceFilter

@swagger_auto_schema(request_body=ProductSerializer)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    filterset_class = ProductPriceFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
    
    @action(['GET', 'POST'], detail=True)
    def like(self, request, pk=None):
        product = self.get_object()
        user = request.user

        try:
            like = Like.objects.filter(product_id=product, User=user)
            mauler = not like[0].like
            if mauler:
                like[0].save()
            else:
                like.delete()
            message = 'Likes' if like else 'Dislike'
        except IndexError:
            Like.objects.create(product_id=product.id, User=user, like=True)
            message = 'Нравится'
        return Response(message, status=200)

    @action(['GET', 'POST'], detail=True)
    def favorite(self, request, pk=None):
        product = self.get_object()
        user = request.user
        try:
            favorites = Favorites.objects.filter(product_id=product, User=user)
            mauler = not favorites[0].favorites
            if mauler:
                favorites[0].save()
            else:
                favorites.delete()
            message = 'In favorites' if favorites else 'Not in favorites'
        except IndexError:
            Favorites.objects.create(product_id=product.id, User=user, favorites=True)
            message = 'In favorites'
        return Response(message, status=200)


@swagger_auto_schema(request_body=ReviewSerializer)
class CommentViewSet(ModelViewSet):
    queryset = CommentRating.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()

# для загрузки большего кол-во изображений
# @swagger_auto_schema(request_body=ImageSerializer)
# class ImageView(ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

@swagger_auto_schema(request_body=CategorySerializer)
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


@swagger_auto_schema(request_body=BrandSerializer)
class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['destroy', 'update', 'partial_update', 'create']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


# @swagger_auto_schema(request_body=ProductSerializer)
# class LikeViewSet(ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer


# @swagger_auto_schema(request_body=ProductSerializer)
# class FavoritesViewSet(ModelViewSet):
#     queryset = Favorites.objects.all()
#     serializer_class = FavoritesSerializer