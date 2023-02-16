from django.urls import path

from ..views import get_current_order, add_item_to_order

urlpatterns = [
    path('', get_current_order, name='order'),
    path('add/', add_item_to_order, name='add_order')
]