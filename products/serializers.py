from multiprocessing import context
from rest_framework import serializers

from .models import Product, CommentRating, Brand, Category, Like, Favorites


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['rating'] = ReviewSerializer(instance.comments.all(), many=True).data
        rep['comments'] = ReviewSerializer(instance.comments.all(), many=True).data
        # rep['image'] = ImageSerializer(instance.boots_image.all(), many=True, context=self.context).data # для загрузки большего кол-во изображений
        rep['like'] = LikeSerializer(instance.like.all(), many=True).data
        rep['favorites'] = FavoritesSerializer(instance.favorites.all(), many=True).data
        
        rating = [dict(i)['rating'] for i in rep['rating']]
        like = sum([dict(i)['like'] for i in rep['like']])
        rep['like'] = like
        favorites = sum([dict(i)['favorites'] for i in rep['favorites']])
        rep['favorites'] = favorites
        
        try:
            rep['rating'] = round((sum(rating) / len(rating)), 2)
            return rep
        except:
            rep['rating'] = None
            return rep


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = CommentRating
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user

        return super().create(validated_data)


# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields =  ['boots', 'image', 'id']

#     def get_image_url(self, obj):
#         if obj.image:
#             url = obj.image.url
#             request = self.context.get('request')
#             if request is not None:
#                 url = request.build_absolute_uri(url)
#         else:
#             url = ''
#         return url

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['image'] = self.get_image_url(instance)

#         return representation

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['author', 'product', 'favorites']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title']
