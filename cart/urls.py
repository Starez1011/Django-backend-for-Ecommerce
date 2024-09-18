from django.urls import path
from cart import views
urlpatterns = [
    path('cart/',views.CartGetView.as_view()),
    path('cart/create',views.CartPostView.as_view()),
    path('cart/delete',views.CartDeleteView.as_view()),
    path('cart/update',views.CartPutView.as_view()),
]