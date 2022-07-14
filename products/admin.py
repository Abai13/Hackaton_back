from django.contrib import admin
from products.models import Brand, Product, SneakersType, CommentRating, Image, Like, Favorites


admin.site.register(Product)
admin.site.register(SneakersType)
admin.site.register(Brand)
admin.site.register(CommentRating)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Favorites)