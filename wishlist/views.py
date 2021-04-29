from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_wishlist(request):
    """ A view to return the shopping wishlist information page """

    return render(request, 'wishlist/wishlist.html')

def add_to_wishlist(request, item_id):
    """ Add a quantity of the identified product to the shopping list busket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})

    if item_id in list(wishlist.keys()):
        wishlist[item_id] += quantity
    else:
        wishlist[item_id] = quantity

    request.session['wishlist'] = wishlist
    print(request.session['wishlist'])
    return redirect(redirect_url)


def edit_wishlist(request, item_id):
    """ Update a quantity of the identified product  and update the total bucket amount """
    quantity = int(request.POST.get('quantity'))
    wishlist = request.session.get('wishlist', {})

    if quantity > 0:
        wishlist[item_id] = quantity
    else:
        wishlist.pop[item_id]

    request.session['wishlist'] = wishlist
    return redirect(reverse('view_wishlist'))


def remove_in_wishlist(request, item_id):
    """ delete a quantity of the identified product and update the total bucket amount"""
    
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        wishlist = request.session.get('wishlist', {}) 

        if wishlist[item_id]:
                wishlist.pop(item_id)
        else:
            wishlist.pop(item_id)

        request.session['wishlist'] = wishlist
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)