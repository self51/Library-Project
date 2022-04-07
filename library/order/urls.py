from django.urls import path
from . import views
from .views import OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('myorders/<int:pk>/', views.user_orders, name='user_orders'),
    path('add/<int:pk>/', views.order_form, name='order_form'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete')
]