from .views import *
from django.urls import path


urlpatterns = [
    path('user/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('product/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('product/<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
    path('review/', ReviewProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list'),
    path('review/<int:pk>/', ReviewProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review-detail'),
    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating-list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='rating-detail'),
    path('cart/', CartViewSet.as_view({'get': 'retrieve'}), name='cart-detail'),
    path('cart_items/', CartItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_item-list'),
    path('cart_items/<int:pk>/', CartItemViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]