from django.urls import path
from ..views import ItemView

urlpatterns = [
    path('<int:id>/', ItemView.as_view(), name='item'),
]