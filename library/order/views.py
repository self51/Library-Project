from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.cache import cache

from .models import Order
from book.models import Book
from .forms import OrderForm


class OrderListView(ListView):
    context_object_name = 'orders'
    model = Order


def user_orders(request, pk):
    orders = cache.get('orders')
    if not orders:
        user = User.objects.get(id=pk)
        orders = Order.objects.filter(user=user)
        cache.set('orders', orders, 60)

    return render(request, 'order/user_orders.html', {'orders': orders})


def order_form(request, pk=None):
    if request.user.is_authenticated:
        book = Book.objects.get(id=pk)
        form = OrderForm(request.POST)

        if form.is_valid() and book.count > 0:
            order = form.save(commit=False)
            order.user = request.user
            order.book = book
            form.save()

            book.count -= 1
            book.save()

        else:
            messages.warning(request, 'Not available now')
            return redirect('/book/')

        return redirect('user_orders', pk=request.user.id)
    return redirect('login')


def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    book = order.book
    book.count += 1
    book.save()

    messages.success(request, 'The book was successfully returned!')
    return redirect('user_orders', pk=request.user.id)