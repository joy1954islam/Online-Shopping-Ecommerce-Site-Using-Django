from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    path('order-view/', views.order_view, name='order_view')
]
