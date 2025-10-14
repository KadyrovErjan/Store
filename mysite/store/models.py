from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

STATUS_CHOICES = (
    ('simple', 'simple'),
    ('silver', 'silver'),
    ('gold', 'gold')
)


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(default='+996')
    data_registered = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.username



class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Product(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    image_product = models.ImageField(upload_to='image_product')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'


    def __str__(self):
        return f'{self.owner} - {self.product_name}'

class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='all_image_product')
    image_product = models.ImageField(upload_to='image_product')

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    stars = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ], null=True, blank=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинг'


    def __str__(self):
        return f'{self.user}'

class ReviewProduct(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    text = models.TextField(null=True, blank=True)
    otvet = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'

    def __str__(self):
        return f'{self.user}'


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        total_price = sum(item.get_total_price() for item in self.items.all())
        discount = 0

        if self.user.status == 'gold':
            discount = 0.75
        if self.user.status == 'silver':
            discount = 0.50
        if self.user.status == 'bronze':
            discount = 0.25

        final_price = total_price * (1 - discount)
        return final_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.cart}'







