from django.urls import path

from ..views import buy, buy_order


urlpatterns = [
    path('<int:id>/', buy, name='buy'),
    path('order/', buy_order, name='buy_order'), 
]