from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from wishlist.contexts import wishlist_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    wishlist = request.session.get('wishlist', {})
    if not wishlist:
        messages.error(
        request, "Oops, seems something the basket list is empty!")
        return redirect(reverse('products'))

    current_wishlist = wishlist_contents(request)
    total = current_wishlist['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request, ('Missing stripe public key, please check your environement variables.!'))

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
