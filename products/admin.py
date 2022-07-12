from django.contrib import admin

from products.models import Brand, Comment, Product, SneakersType

admin.site.register(Product)
admin.site.register(SneakersType)
admin.site.register(Brand)
admin.site.register(Comment)