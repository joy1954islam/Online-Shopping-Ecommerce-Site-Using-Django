from django.conf.urls import url
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('signup/', views.register, name='signup'),
    path('change/profile/', views.ChangeProfile, name='change_profile'),

]