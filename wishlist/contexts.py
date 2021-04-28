from decimal import Decimal
from django import settings

def wishlist_contents(request):
    
    wishlist_items = []
    total = 0
    product_count = 0

    grand total = total

    context = {
        'wishlist_items': wishlist_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context


    context = {}

    return context