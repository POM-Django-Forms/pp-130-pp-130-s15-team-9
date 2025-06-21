from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order
from .forms import OrderForm

class OrderList(ListView):
    model = Order
    template_name = 'order/orders_list.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        user_id = self.request.GET.get('user')
        if user_id:
            qs = qs.filter(user_id=user_id)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        from authentication.models import CustomUser
        ctx['users'] = CustomUser.objects.all()
        ctx['selected_user'] = self.request.GET.get('user', '')
        return ctx

class UserOrders(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/my_orders.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class MakeOrder(LoginRequiredMixin, View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'order/make_order.html', {
            'form': form
        })

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('my-orders')
        return render(request, 'order/make_order.html', {
            'form': form
        })

class OrderReturn(View):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        if not order.end_at:
            order.end_at = timezone.now()
            order.save()
        return redirect('orders_list')