from rest_framework import serializers

from .models import Comment, Product

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['rating']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        rep['rating'] = ReviewSerializer(instance.review.all(), many=True).data
        rat = [dict(i)['rating'] for i in rep['rating']]
        if rat:
            rep['rating'] = round((sum(rat) / len(rat)), 2)
            return rep
        else:
            rep['rating'] = None
            return rep


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = ['author', 'text', 'rating', 'create_date', 'id']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user

        return super().create(validated_data)