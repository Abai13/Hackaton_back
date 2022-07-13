# Generated by Django 4.0.5 on 2022-07-13 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('total_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('open', 'Открытый'), ('in_process', 'В обработке'), ('canceled', 'Отмененный'), ('finished', 'Завершенный')], default='open', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='productcs',
            field=models.ManyToManyField(through='orders.OrderItems', to='products.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
