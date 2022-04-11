from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Order
from book.models import Book
from .forms import OrderForm


class OrderListView(ListView):
    context_object_name = 'orders'
    model = Order


def user_orders(request, pk):
    user = User.objects.get(id=pk)
    orders = Order.objects.filter(user=user)
    return render(request, 'order/user_orders.html', {'orders': orders})

def order_form(request, pk=None):
    if request.user.is_authenticated:
        book = Book.objects.get(id=pk)
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.book = book
            form.save()
        return redirect('/order/')
    return redirect('login')

def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('account')