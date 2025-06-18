from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from .models import Order
from django.utils.dateparse import parse_datetime
from authentication.models import CustomUser
from book.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin

class OrderList(ListView):
    model = Order
    template_name = 'order/orders_list.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.GET.get('user')

        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all()
        context['selected_user'] = self.request.GET.get('user')
        return context

class UserOrders(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order/my_orders.html"
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class MakeOrder(View):
    def post(self, request):
        book_id = int(request.POST.get('book_id'))
        book = Book.objects.get(id=book_id)

        planned_return = request.POST.get('planned_return')
        planned_return_dt = parse_datetime(planned_return)

        Order.create(user=request.user, book=book, plated_end_at=planned_return_dt)


        return redirect('my-orders')

class OrderReturn(View):
    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        if not order.end_at:
            order.end_at = timezone.now()
            order.save()
        return redirect('orders_list')