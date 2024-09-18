from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from .models import Product, Category
from rest_framework.response import Response
from rest_framework import status
from accounts.mixins import IsAdminMixin, IsNormalUsersMixin, IsStaffUsersMixin

class CategoryGetView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryPostView(IsAdminMixin,IsStaffUsersMixin,APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'info': 'Category created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class CategoryDeleteView(IsAdminMixin,IsStaffUsersMixin,APIView):
    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return Response({'info': 'Category deleted'}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

class CategoryPutView(IsAdminMixin,IsStaffUsersMixin,APIView):
    def put(self, request):
        id = request.data.get('id')
        if id is None:
            return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'info': 'Category updated'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
class CategorywiseProductGetView(APIView):
    def get(self, request):
        try:
            category = request.GET.get('categoryId')
            if not category:
                return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
            products = Product.objects.filter(category__id=category).order_by('-date_added')
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'An error occurred while fetching category-wise products.'}, status=status.HTTP_400_BAD_REQUEST)
class ProductGetAllView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductGetView(IsAdminMixin,IsStaffUsersMixin,IsNormalUsersMixin,APIView):
    def get(self, request):
        id = request.GET.get('id')
        if id is None:
            return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
class ProductPostView(IsAdminMixin,IsStaffUsersMixin,APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'info': 'Product created'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
class ProductDeleteView(IsAdminMixin,IsStaffUsersMixin,APIView):
    def delete(self, request):
        id = request.GET.get('id')
        if id is None:
            return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({'info': 'Product deleted'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
class ProductPutView(IsAdminMixin,IsStaffUsersMixin,APIView):
    def put(self, request):
        id = request.data.get('id')
        if id is None:
            return Response({'error': 'Invalid ID'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'info': 'Product updated'}, status=status.HTTP_200_OK)
            return Response({'error': 'Product Update Invalid'}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
class ProductSearchView(APIView):
    def get(self, request):
        try:
            query = request.GET.get('query')
            if query is None:
                return Response({'error': 'Search parameter is missing.'}, status=status.HTTP_400_BAD_REQUEST)
            products = Product.objects.filter(name__icontains=query).order_by('-date_added')
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)