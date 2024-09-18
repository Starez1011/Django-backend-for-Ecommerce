from django.shortcuts import render
from accounts.mixins import IsNormalUsersMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer, CartItemSerializer
from products.models import Product

class CartGetView(IsNormalUsersMixin,APIView):
    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CartPostView(IsNormalUsersMixin,APIView):
    def post(self, request):
        try:
            product_id = request.data.get('product_id')
            quantity = request.data.get('quantity',1)
            
            if quantity <= 0:
                return Response({'error': 'Quantity must be greater than zero'}, status=status.HTTP_400_BAD_REQUEST)
            
            products = Product.objects.get(id=product_id)
            cart, _ = Cart.objects.get_or_create(user=request.user)
            cartItem, item_created = CartItem.objects.get_or_create(cart=cart, product=products)
            if not item_created:
                cartItem.quantity += quantity
            else:
                cartItem.quantity = quantity
            cartItem.save()

            serializer = CartSerializer(cart) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'error': 'Invalid quantity value'}, status=status.HTTP_400_BAD_REQUEST)

class CartDeleteView(IsNormalUsersMixin,APIView):
    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            cartItem = CartItem.objects.get(id=id,cart__user = request.user)
            cartItem.delete()
            return Response({'info': 'Item removed from cart'}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
class CartPutView(IsNormalUsersMixin,APIView):
    def put(self, request):
        id = request.GET.get('id')
        if id is None:
            return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            cartItem = CartItem.objects.get(id=id,cart__user = request.user)
            quantity = int(request.data.get('quantity',1))
            
            if quantity <= 0:
                return Response({'error': 'Quantity must be greater than zero'}, status=status.HTTP_400_BAD_REQUEST)
            
            if quantity == 0:
                cartItem.delete()
                return Response({'info': 'Cart item removed'}, status=status.HTTP_204_NO_CONTENT)
            # Update the cart item
            serializer = CartItemSerializer(cartItem, data={'quantity': quantity}, partial=True)
            if serializer.is_valid():
                serializer.save()
                cart = Cart.objects.get(user=request.user)
                cart_serializer = CartSerializer(cart)
                return Response(cart_serializer.data, status=status.HTTP_200_OK)
            return Response({'error':'invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({'error': 'Invalid quantity value'}, status=status.HTTP_400_BAD_REQUEST)



