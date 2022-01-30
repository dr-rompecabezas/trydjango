from django.urls import path
from .views import (
    dynamic_lookup_view, 
    product_delete_view,
    product_create_view, 
    product_list_view)

app_name = 'products' # namespacing
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:id>/', dynamic_lookup_view, name='product-lookup'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]