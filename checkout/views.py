from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    wishlist = request.session.get('bag', {})
    if not wishlist:
        messages.error(
        request, "Oops, seems something went wrong!")
        return redirect(reverse('products'))

    order_form = orderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
