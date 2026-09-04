from django.urls import path
from . import views

urlpatterns = [

    path("products/", views.products, name="products"),

    path("products/",views.product_detail,name="product_detail"),

    path("cart/",views.cart,name="cart"),

    path("add-cart/",views.add_to_cart,name="add_to_cart"),

    path("chatbot/",views.chatbot_view,name="chatbot")
    
]