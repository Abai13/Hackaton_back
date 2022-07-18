from django.contrib import admin
from products.models import Brand, Product, Category, CommentRating, Like, Favorites #Image


# для загрузки большего кол-во изображений
# class ProductImageInLine(admin.TabularInline):
#     # model = Image
#     max_num = 10
#     min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    # inlines = [ProductImageInLine, ] # для загрузки большего кол-во изображений


# admin.site.register(Product) # для загрузки большего кол-во изображений
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CommentRating)
# admin.site.register(Image) # для загрузки большего кол-во изображений
admin.site.register(Like)
admin.site.register(Favorites)