from django.shortcuts import get_object_or_404
from products.models import Product

def wishlist_contents(request):
    
    wishlist_items = []
    total = 0
    product_count = 0
    wishlist = request.session.get('wishlist', {})

    for item_id, quantity in wishlist.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        wishlist_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = total

    context = {
        'wishlist_items': wishlist_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
