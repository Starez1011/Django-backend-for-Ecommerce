from django.urls import path
from products import views

urlpatterns = [
    path('product/create/',views.ProductPostView.as_view()),
    path('product/delete/',views.ProductDeleteView.as_view()),
    path('product/update/',views.ProductPutView.as_view()),
    path('all-products/',views.ProductGetAllView.as_view()),
    path('products/',views.ProductGetView.as_view()),

    path('category/',views.CategoryGetView.as_view()),
    path('category/create/',views.CategoryPostView.as_view()),
    path('category/delete/',views.CategoryDeleteView.as_view()),
    path('category/update/',views.CategoryPutView.as_view()),
]