# Generated by Django 4.0.5 on 2022-07-15 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Сategories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('gender', models.CharField(blank=True, choices=[('all', 'Все'), ('male', 'Мужские'), ('female', 'Женские')], default='Все', max_length=20)),
                ('size', models.IntegerField(blank=True, choices=[(35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'), (46, '46'), (47, '47')])),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brand', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.brand')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.category')),
            ],
            options={
                'verbose_name': 'Sneakers',
                'verbose_name_plural': 'Sneakers',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(blank=True, default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='products.product')),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('boots', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boots_image', to='products.product')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorites', models.BooleanField(blank=True, default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='products.product')),
            ],
            options={
                'verbose_name': 'Favorite',
                'verbose_name_plural': 'Favorites',
            },
        ),
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, choices=[(1, '⭐️'), (2, '⭐️⭐️'), (3, '⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (5, '⭐️⭐️⭐️⭐️⭐️')], null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-create_date'],
            },
        ),
    ]
