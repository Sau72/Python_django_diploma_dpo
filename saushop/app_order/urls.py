from django.urls import path
from app_order.api import OrderCreateView, PaymentListView, BasketListView, OrdersView

app_name = "app_order"

urlpatterns = [
    # path('api/orders/', OrderListView.as_view(), name='orders_get'),
    path("api/orders", OrderCreateView.as_view(), name="orders_post"),
    path("api/order/<int:pk>/", OrdersView.as_view(), name="order"),
    path("api/order/<int:pk>", OrdersView.as_view(), name="order_confirm"),
    path("api/payment/<int:pk>", PaymentListView.as_view(), name="payment"),
    path("api/basket", BasketListView.as_view(), name="basket"),
]
