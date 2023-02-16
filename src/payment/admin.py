from django.contrib import admin

from .models import Item, Order

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('name', 'price')
    list_display_links = ('name',)
    
    
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('user', 'item')
    
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)