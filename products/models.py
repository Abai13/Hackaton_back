from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

class Brand(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Brand, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'


class SneakersType(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(SneakersType, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Product(models.Model):
    MALE_CHOICE = (
        ('all', 'Все'),
        ('male', 'Мужские'),
        ('female', 'Женские'),
    )

    SIZE_CHOICE = (
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
    )

    title = models.CharField(max_length=155)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product')
    sneakers_type = models.ForeignKey(SneakersType, on_delete=models.CASCADE, related_name='product')
    male = models.CharField(max_length=20, choices=MALE_CHOICE, default='Все')
    size = models.CharField(max_length=20, choices=SIZE_CHOICE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'


class Comment(models.Model):
    RATING_CHOICE = (
        (1, '⭐️'),
        (2, '⭐️⭐️'),
        (3, '⭐️⭐️⭐️'),
        (4, '⭐️⭐️⭐️⭐️'),
        (5, '⭐️⭐️⭐️⭐️⭐️'),
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='review')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    rating = models.CharField(max_length=5, choices=RATING_CHOICE, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment from {self.author.title} to {self.product}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-create_date']