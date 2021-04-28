from django.shortcuts import render, redirect

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