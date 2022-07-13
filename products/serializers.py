from rest_framework import serializers

from .models import Product, CommentRating


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['rating'] = ReviewSerializer(instance.comments.all(), many=True).data
        rep['comments'] = ReviewSerializer(instance.comments.all(), many=True).data

        rating = [dict(i)['rating'] for i in rep['rating']]
        if rating:
            rep['rating'] = round((sum(rating) / len(rating)), 2)
            return rep
        else:
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