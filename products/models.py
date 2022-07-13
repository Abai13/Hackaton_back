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
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class SneakersType(models.Model):
    title = models.CharField(max_length=150, primary_key=True)
    slug = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(SneakersType, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Type'
        verbose_name_plural = 'Types'


class Product(models.Model):

    SIZE_CHOICE = (
        (35, '35'),
        (36, '36'),
        (37, '37'),
        (38, '38'),
        (39, '39'),
        (40, '40'),
        (41, '41'),
        (42, '42'),
        (43, '43'),
        (44, '44'),
        (45, '45'),
        (46, '46'),
        (47, '47'),
    )

    GENDER_CHOICE = (
        ('all', 'Все'),
        ('male', 'Мужские'),
        ('female', 'Женские'),
    )

    title = models.CharField(max_length=155)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product')
    category = models.ForeignKey(SneakersType, on_delete=models.CASCADE, related_name='product')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='Все')
    size = models.IntegerField(choices=SIZE_CHOICE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', null=True, blank=True)
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Sneakers'
        verbose_name_plural = 'Sneakers'


class CommentRating(models.Model):
    rating_choices = (
    (1, '⭐️'),
    (2, '⭐️⭐️'),
    (3, '⭐️⭐️⭐️'),
    (4, '⭐️⭐️⭐️⭐️'),
    (5, '⭐️⭐️⭐️⭐️⭐️'),
    )
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=rating_choices, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.rating and self.text:
            return f'Комментарий и рейтинг от {self.author.name} к {self.product}'
        elif self.rating:
            return f'Рейтинг от {self.author.name} к {self.product}'
        elif self.text:
            return f'Комментарий от {self.author.name} к {self.product}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-create_date']