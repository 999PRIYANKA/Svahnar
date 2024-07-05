from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart, Order, CartProduct, OrderProduct

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # user = User.objects.create_user(**validated_data)
         user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
         return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products']

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total_price', 'created_at']
