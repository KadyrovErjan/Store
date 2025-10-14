from rest_framework.response import Response
from .models import *
from .permissions import CheckPermissions, MethodCheck
from .serializers import *
from rest_framework import viewsets
from .filters import ProductFilters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from .pagination import ProductPagination, RatingPagination

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilters
    search_fields = ['product_name']
    ordering_fields = ['product_name', 'price']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = ProductPagination


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, MethodCheck]

class ImageProductViewSet(viewsets.ModelViewSet):
    queryset = ImageProduct.objects.all,()
    serializer_class = ImageProductSerializers

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = RatingPagination

class ReviewProductViewSet(viewsets.ModelViewSet):
    queryset = ReviewProduct.objects.all()
    serializer_class = ReviewProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckPermissions]

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializers

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializers.data)

class CartItemViewSet(viewsets.ModelViewSet):
    serializers_class = CartItemSerializers

    def get_queryset(self):
        return CartItem.objects.filter(cart_user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


