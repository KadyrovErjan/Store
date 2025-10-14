from .models import *
from rest_framework import serializers


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    owner = UserProfileSerializers()
    class Meta:
        model = Product
        fields = ['id', 'owner', 'category', 'product_name', 'image_product', 'price']


class ImageProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageProduct
        fields = '__all__'




class ReviewProductSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    product = ProductSerializers()
    created_at = serializers.DateTimeField(format('%d-%m-%Y-%H:%M'))
    class Meta:
        model = ReviewProduct
        fields = ['id', 'user', 'product', 'text', 'otvet', 'created_at']

class ReviewProductSimpleSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    created_at = serializers.DateTimeField(format('%d-%m-%Y-%H-%M'))
    class Meta:
        model = ReviewProduct
        fields = ['id', 'user', 'text', 'otvet', 'created_at']

class RatingSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers(read_only=True)
    product = ProductSerializers()
    class Meta:
        model = Rating
        fields = ['id', 'user', 'product', 'stars']

class RatingSimpleSerializers(serializers.ModelSerializer):
    user = UserProfileSerializers()
    class Meta:
        model = Rating
        fields = ['id', 'user', 'stars']

class ProductDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    review = ReviewProductSimpleSerializers(read_only=True, many=True)
    all_image_product = ImageProductSerializers(read_only=True, many=True)
    rating = RatingSimpleSerializers(read_only=True, many=True)
    owner = UserProfileSerializers()
    class Meta:
        model = Product
        fields = ['id', 'category', 'owner', 'product_name', 'image_product', 'all_image_product', 'price', 'description', 'review', 'rating']

class CartItemSerializers(serializers.ModelSerializer):
    product = ProductSerializers(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'get_total_price']

class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(read_only=True, many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()

