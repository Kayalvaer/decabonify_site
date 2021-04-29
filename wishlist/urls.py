from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='view_wishlist'),
    path('add/<item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('edit/<item_id>/', views.edit_wishlist, name='edit_wishlist'),
    path('remove/<item_id>/', views.remove_in_wishlist, name='remove_in_wishlist'),
]