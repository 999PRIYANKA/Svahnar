from django.urls import path
from .views import UserCreate, ProductList, ProductDetail, CartDetail, CartAddProduct, OrderCreate, CustomAuthToken, Logout, CartList

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-create'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('cart/', CartDetail.as_view(), name='cart-detail'),
    path('cart/', CartList.as_view(), name='cart-list'),
    path('cart/add/', CartAddProduct.as_view(), name='cart-add-product'),
    path('order/', OrderCreate.as_view(), name='order-create'),
    path('checkout/', OrderCreate.as_view(), name='order-create'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
