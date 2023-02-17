from typing import Type, Optional

from django.db.models import Model
from django.db.models import QuerySet

from .models import Item


class ItemObjectMixin:
    def get_object(
            self, 
            queryset: Optional[QuerySet] = None) -> Type[Model]:
        if self.model is None:
            self.model: Type[Model] = Item
        return super().get_object(queryset=queryset) #type: ignore