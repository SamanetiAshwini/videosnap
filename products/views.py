import requests
from products.chatbot import URL
from products.models import ChatHistory
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Product
from .models import Cart
from .models import CartItem

from django.http import JsonResponse


# Display all products
def products(request):

    products = Product.objects.all()

    return render(request, "accounts/product.html", {
        "products": products
    })


# Display one product
def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(request, "accounts/product_detail.html", {
        "product": product
    })


# Display cart
@login_required
def cart(request):

    cart = Cart.objects.filter(user=request.user).first()

    items = []
    total = 0

    if cart:

        items = CartItem.objects.filter(cart=cart)

        for item in items:
            total += item.product.price * item.quantity

    return render(request, "accounts/cart.html", {
        "items": items,
        "total": total
    })


# Add product to cart
@login_required
def add_to_cart(request, id):

    product = Product.objects.get(id=id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart")


# Chatbot View
def chatbot_view(request):
    if request.method == "POST":
        # Handle text messages
        user_message = request.POST.get("message")
        if not user_message:
            # Maybe it's raw JSON from fetch
            import json
            try:
                body = json.loads(request.body)
                user_message = body.get("message")
            except Exception:
                pass

        if not user_message:
            return JsonResponse({"error": "Message is required"}, status=400)

        # Call Gemini API
        from products.chatbot import URL
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": user_message}
                    ]
                }
            ]
        }

        bot_response = "Sorry, I am having trouble connecting to the AI helper."
        try:
            res = requests.post(URL, json=data, headers=headers)
            if res.status_code == 200:
                res_data = res.json()
                bot_response = res_data['candidates'][0]['content']['parts'][0]['text']
            else:
                bot_response = f"API Error (Status {res.status_code}): {res.text}"
        except Exception as e:
            bot_response = f"Exception occurred: {str(e)}"

        # Save conversation to history
        ChatHistory.objects.create(
            user_input=user_message,
            text_output=bot_response
        )

        return JsonResponse({"response": bot_response})

    # GET request - return template with history
    history = ChatHistory.objects.all().order_by("created_at")
    return render(request, "accounts/chatbot.html", {"history": history})