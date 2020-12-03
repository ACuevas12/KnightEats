from django.db.models import Sum
from django.views import generic
from django.shortcuts import render

from .models import Order, Item, Simple, ItemMenu, ItemCategory
from .forms import TestForm, ItemRequestForm, NewOrderForm, SearchBoxForm, CategoryForm, PaymentForm

from datetime import datetime


class SeeActiveOrders(generic.ListView):
    template_name = 'ordering/orders.html'
    context_object_name = 'my_orders'

    def get_queryset(self):
        return Order.objects.filter(
            user__username__contains=self.request.user.username
        ).filter(
            order_finished=False
        )


class SeeFinishedOrders(generic.ListView):
    template_name = 'ordering/orders_pay.html'
    context_object_name = 'my_orders'

    def get_queryset(self):
        return Order.objects.filter(
            user__username__contains=self.request.user.username
        ).filter(
            order_finished=True
        ).filter(
            order_archived=False
        )


def PayForOrder(request):
    payment_form = PaymentForm()
    context = {
        'form_pay': payment_form
    }
    if request.method == "POST":
        if '_payOrder' in request.POST:
            payment_form = PaymentForm(request.POST)
            if payment_form.is_valid():
                q = payment_form.cleaned_data['payment_order']
                o = Order.objects.get(order_num__exact=q)
                o.order_paid = True
                o.save()

    return render(request, 'ordering/payment_complete.html', context)


class SeeArchivedOrders(generic.ListView):
    template_name = 'ordering/orders.html'
    context_object_name = 'my_orders'

    def get_queryset(self):
        return Order.objects.filter(
            user__username__contains=self.request.user.username
        ).filter(
            order_archived=True
        )


class ViewItems(generic.ListView):
    template_name = 'ordering/items_list.html'
    context_object_name = 'my_items'

    def get_context_data(self, **kwargs):
        context = super(ViewItems, self).get_context_data(**kwargs)
        order_sum = Item.objects.filter(
            on_order__order_num__exact=self.kwargs['order_num']
        ).aggregate(Sum('item_price')).get('item_price__sum')
        context.update({
            'store': self.kwargs['order_num'],
            'order_total': order_sum,
            'order_tax': order_sum * .07,
            'order_after_tax': order_sum * 1.07,
            'time_placed': getattr(Order.objects.get(order_num__exact=self.kwargs['order_num']), 'order_time'),
        })
        return context

    def get_queryset(self):
        exact_num = self.kwargs['order_num']
        return Item.objects.filter(
            on_order__order_num__exact=exact_num
        )


def ViewMenu(request):
    order_form = NewOrderForm()
    item_form = ItemRequestForm()
    search_form = SearchBoxForm()
    category_form = CategoryForm()
    context = {
        'menu': Item.objects.filter(
            on_menu__menu_name__exact="Active Menu"
        ),
        'form': order_form,
        'form2': item_form,
        'form3': search_form,
        'form4': category_form,
    }

    if request.method == "POST":
        if '_newOrder' in request.POST:
            order_form = NewOrderForm(request.POST)
            if order_form.is_valid():
                order_to_change = order_form.cleaned_data['new_order_num']
                new_order = Order(
                    user=request.user,
                    order_num=order_to_change,
                    order_time=datetime.now(),
                    order_finished=False,
                )
                new_order.save()
        elif '_newItem' in request.POST:
            item_form = ItemRequestForm(request.POST)
            if item_form.is_valid():
                item_quantity = item_form.cleaned_data['item_quantity']
                order_number_sent = item_form.cleaned_data['add_to_order']

                item_clone = Item(
                    item_name=request.POST.get('_itemName'),
                    item_quantity=item_quantity,
                    item_price=request.POST.get('_itemPrice'),
                    on_order=Order.objects.get(order_num__exact=order_number_sent),
                    on_menu=ItemMenu.objects.get(menu_name__exact="Ordered Menu"),
                    on_category=ItemCategory.objects.get(category_name__exact=request.POST.get('_itemCategory')),
                )
                item_clone.save()

    if '_searchField' in request.POST:
        search_form = SearchBoxForm(request.POST)
        if search_form.is_valid():
            search_query = search_form.cleaned_data['search_field']
            context.update({
                'menu': Item.objects.filter(
                    on_menu__menu_name__exact="Active Menu"
                ).filter(item_name__contains=search_query),
                'form': order_form,
                'form2': item_form,
                'form3': search_form,
                'form4': category_form,
            })
            return render(request, 'ordering/menu_list.html', context)

    if '_categoryField' in request.POST:
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_chosen = category_form.cleaned_data['category_choice']
            context.update({
                'menu': Item.objects.filter(
                    on_menu__menu_name__exact="Active Menu"
                ).filter(on_category__category_name__exact=category_chosen),
                'form': order_form,
                'form2': item_form,
                'form3': search_form,
                'form4': category_form,
            })
            return render(request, 'ordering/menu_list.html', context)
    else:
        return render(request, 'ordering/menu_list.html', context)


def get_number(request):
    form = TestForm()

    if request.method == "POST":
        if '_single' in request.POST:
            form = TestForm(request.POST)
            if form.is_valid():
                n = form.cleaned_data['test_field']
                t = Simple(simple_integer=n)
                t.save()
        elif '_double' in request.POST:
            form = TestForm(request.POST)
            if form.is_valid():
                n = form.cleaned_data['test_field']
                t = Simple(simple_integer=n)
                tt = Simple(simple_integer=n)
                t.save()
                tt.save()

    return render(request, 'separate/temporary_view.html', {
        'form': form
    })


def clone_order(request):
    form = ItemRequestForm()

    if request.method == "POST":
        form = ItemRequestForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['item_quantity']
            item_clone = Item(
                item_name="Shot of Bourbon",  # Change later to match displayed item
                item_quantity=n,
                item_price=20,  # change to match price of displayed
                on_order=Order.objects.get(order_num__exact=6465),  # change to match order being placed on
                on_menu=ItemMenu.objects.get(menu_name__exact="Active Menu"),
                on_category=ItemCategory.objects.get(category_name__exact="Drinks"),  # change to match category
            )
            item_clone.save()

    return render(request, 'separate/temporary_view_two.html', {
        'form': form
    })


def place_new_order(request):
    form = NewOrderForm()
    form2 = ItemRequestForm()

    context = {
        'menu': Item.objects.filter(
            on_menu__menu_name__exact="Active Menu"
        ),
        'form': form,
        'form2': form2,
    }

    if request.method == "POST":
        if '_newOrder' in request.POST:
            form = NewOrderForm(request.POST)
            if form.is_valid():
                m = form.cleaned_data['new_order_num']
                new_order = Order(
                    user=request.user,
                    order_num=m,
                    order_time=datetime.now(),
                    order_finished=False,
                )
                new_order.save()
        elif '_newItem' in request.POST:
            form2 = ItemRequestForm(request.POST)
            if form2.is_valid():
                n = form2.cleaned_data['item_quantity']
                o = form2.cleaned_data['add_to_order']

                item_clone = Item(
                    item_name=request.POST.get('_itemName'),
                    item_quantity=n,
                    item_price=request.POST.get('_itemPrice'),
                    on_order=Order.objects.get(order_num__exact=o),
                    on_menu=ItemMenu.objects.get(menu_name__exact="Active Menu"),
                    on_category=ItemCategory.objects.get(category_name__exact=request.POST.get('_itemCategory')),
                )
                item_clone.save()

    return render(request, 'separate/must_go_deeper.html', context)
