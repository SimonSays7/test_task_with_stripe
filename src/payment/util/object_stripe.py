from typing import Dict, Any, List
from collections.abc import Sequence, Iterable

import stripe
from stripe.api_resources.checkout import Session

from django.db.models import Model

from ..models import Item, Order


def create_line_items(product: Iterable) -> List[Dict[str, Any]]:
    line_items: List[Dict[str, Any]] = []
    for item in product:
        items = {
            'price_data':{
                'currency': 'usd',
                'product_data': {
                    'name': item['item__name'],
                },
                'unit_amount': item['item__price']
            },
            'quantity': item['sum'],
        }
        line_items.append(items)
    return line_items


def create_one_line_items(product: Item) -> List[Dict[str, Any]]:
    line_items: List[Dict[str, Any]] = []
    items = {
        'price_data':{
        'currency': 'usd',
            'product_data': {
                'name': product.name,
            },
            'unit_amount': product.price
        },
        'quantity': 1,
    }
    line_items.append(items)
    return line_items


def create_stripe_session(line_items: List[Dict[str, Any]], api_key: str) -> Session:
    session = stripe.checkout.Session.create(
        api_key=api_key,
        mode='payment',
        success_url='http://127.0.0.1:8000/item/1/',
        cancel_url='http://127.0.0.1:8000/item/1/',
        line_items=line_items
    )
    return session