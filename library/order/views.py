from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Order
from .forms import OrderForm


class OrderListView(ListView):
    context_object_name = 'orders'
    model = Order

def order_form(request, pk=None):
    if request.method == 'GET':
        if pk == None:
            form = OrderForm()
        else:
            order = Order.objects.get(pk)
            form = OrderForm(instance=order)
        return render(request, 'order/order_form.html', {'form': form})
    else:
        if pk == None:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save(commit=False).user = request.user
            form.save()
        return redirect('/order/')

def order_delete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('/order/')