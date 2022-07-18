from django.contrib import admin
from products.models import Brand, Product, Category, CommentRating, Like, Favorites


# class ProductImageInLine(admin.TabularInline):
#     # model = Image
#     max_num = 10
#     min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    # inlines = [ProductImageInLine, ]


# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CommentRating)
# admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Favorites)