from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('Hub/', TemplateView.as_view(template_name='ordering/hub.html'), name='hub'),
    path('MyThings/', TemplateView.as_view(template_name='my_things.html'), name='my_things'),
    path('PaidOrder/', views.PayForOrder, name='paid_order'),
    path('Active_Orders/', views.SeeActiveOrders.as_view(), name='order_list'),
    path('Completed_Orders/', views.SeeFinishedOrders.as_view(), name='finished_order_list'),
    path('Archived_Orders/', views.SeeArchivedOrders.as_view(), name='archived_order_list'),
    path('View_Items/<int:order_num>/', views.ViewItems.as_view(), name='view_order'),
    path('View_Menu/', views.ViewMenu, name='view_menu'),
    path('test_page/', views.get_number, name='test_page'),
    path('test_clone/', views.clone_order, name='clone_page'),
    path('clone_w_context/', views.place_new_order, name='deep_page'),
]
