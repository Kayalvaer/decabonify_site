from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_wishlist(request):
    """ A view to return the shopping wishlist information page """

    return render(request, 'wishlist/wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add a quantity of the identified product to the shopping list basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] += quantity
        messages.success(
            request, f'NB:\
                {product.name} quantity has been updated on {wishlist[item_id]}')
    else:
        wishlist[item_id] = quantity
        messages.success(
            request, f'NB:\
                {product.name} has been added to basket')

    request.session['wishlist'] = wishlist
    print(request.session['wishlist'])
    return redirect(redirect_url)


def edit_wishlist(request, item_id):
    """ Update a quantity of the identified product  and update the total bucket amount """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    wishlist = request.session.get('wishlist', {})

    if quantity > 0:
        wishlist[item_id] = quantity
        messages.success(
            request, f'NB:\
                {product.name} quantity updated to {wishlist[item_id]}')

    else:
        wishlist.pop[item_id]
        messages.success(
            request, f'NB:\
                {product.name} removed out of the basket')

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


def remove_in_wishlist(request, item_id):
    """ delete a quantity of the identified product and update the total bucket amount"""
    
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        wishlist = request.session.get('wishlist', {}) 

        if wishlist[item_id]:
            wishlist.pop(item_id)
            messages.success(
            request, f'NB:\
                {product.name} removed out of the basket')
        else:
            wishlist.pop(item_id)
            messages.success(
            request, f'NB:\
                {product.name} removed out of the basket')

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request, f'Oops! Something went wrong when removing item: {e}')
        return HttpResponse(status=500)