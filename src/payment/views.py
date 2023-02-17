from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseRedirectBase
from django.views.generic.detail import DetailView
from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.http import (
    HttpRequest, 
    HttpResponse, 
    JsonResponse, 
)

from .dependency.data_enviroment import get_api_key_stripe, get_publick_key
from .views_mixin import ItemObjectMixin
from .models import Item, Order
from .util.object_stripe import (
    create_line_items, 
    create_stripe_session, 
    create_one_line_items
)


def buy(request: HttpRequest, id: int) -> JsonResponse:
    api_key = get_api_key_stripe()
    product = get_object_or_404(Item, id=id)
    line_items = create_one_line_items(product)
    session = create_stripe_session(
        line_items=line_items, 
        api_key=api_key
    )
    return JsonResponse({'id': session.id})


def add_item_to_order(request: HttpRequest
        ) -> HttpResponseRedirectBase:
    item_id = request.POST['item']
    print(request.POST['item'])
    item = get_object_or_404(Item, id=item_id)
    order = Order(user=request.user, item=item)
    order.save()
    return redirect(reverse_lazy('item', kwargs={'id': item_id}))


def buy_order(request: HttpRequest) -> JsonResponse:
    api_key = get_api_key_stripe()
    orders = Order.objects.filter(user=request.user
    ).all().values(
        'item__name', 
        'item__price'
    ).annotate(sum=Count('item')
    )
    line_items = create_line_items(orders)
    print(line_items)
    session = create_stripe_session(
        line_items=line_items,
        api_key=api_key)
    return JsonResponse({'id': session.id})


def get_current_order(request: HttpRequest) -> HttpResponse:
    orders = Order.objects.filter(user=request.user).all()
    summary = orders.aggregate(sum=Sum('item__price'))
    context = {
        'orders': orders,
        'sum': summary,
        'stripe_public': get_publick_key()
    }
    return render(request, 'payment/orders.html', context=context)


class ItemView(ItemObjectMixin, DetailView):
    pk_url_kwarg: str = 'id'
    template_name = 'payment/item_detail.html'
    extra_context = {'stripe_public' : get_publick_key()}