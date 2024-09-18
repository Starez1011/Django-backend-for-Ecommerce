from rest_framework import serializers
from .models import Cart, CartItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nested serializer to show product details

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total_price']
    def validate_quantity(self, value):
        # Ensure the quantity is a positive integer
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value
# Cart Serializer
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)  # Updated to handle the ManyToMany relationship

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'get_total_price']
    def get_total_price(self, obj):
        return sum([item.get_total_price() for item in obj.cartitem_set.all()])