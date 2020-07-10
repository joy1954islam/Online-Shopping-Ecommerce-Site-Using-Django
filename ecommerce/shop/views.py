from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

from .forms import UserUpdateForm, UserRegisterForm
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/product/detail.html', context)


def search(request):
    products = Product.objects.filter(name__contains=request.GET['title'])
    return render(request, 'shop/product/search.html', {'products': products})


def login(request):
    if request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user =authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('shop:product_list')
            else:
                return redirect('shop:signup')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'shop/product/login.html',context)


def signoutView(request):
    logout(request)
    return redirect('shop:login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:login')
    else:
        form = UserRegisterForm()
    return render(request, 'shop/product/register.html', {'form': form})


def Profile(request):
    return render(request,'shop/product/profile.html',)


def ChangeProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('shop:change_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'shop/product/change_profile.html', context)

