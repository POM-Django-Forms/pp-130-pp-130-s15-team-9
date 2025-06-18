from django.urls import path
from .views import OrderList, OrderReturn, UserOrders, MakeOrder

urlpatterns = [
    path('orders/', OrderList.as_view(), name='orders_list'),
    path('orders/return/<int:order_id>/', OrderReturn.as_view(), name='mark_order_returned'),
    path('my-orders/', UserOrders.as_view(), name='my-orders'),
    path('make-order/', MakeOrder.as_view(), name='make-order'),
]
