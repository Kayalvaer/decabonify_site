from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    wishlist = request.session.get('wishlist', {})
    if not wishlist:
        messages.error(
        request, "Oops, seems something the basket list is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ilsw4E2NW4zo9nQ2sPcR9Z8koTmzPpgm7fqF1yUGFMKSAWdWYBLptvzzvka8Rt7FgCaLMXJqhqeyxd3QlF5aRen00VcQcvJl5'
    }

    return render(request, template, context)
