from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *



def register(request):
    if request.method == 'POST':
        data = request.POST 
        username = data.get('username')
        password = data.get('password')
        if username and password:
            User.objects.create_user(
                username = username,
                password = password
            )
        return redirect('login_user')
    return render(request,'registration.html')


def login_user(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            request,
            username=data.get('username'),
            password=data.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')
    
    
    
@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')

@login_required
def home(request):
    wallets = Wallet.objects.filter(user=request.user)
    return render(request, 'home.html', {'wallets': wallets})

@login_required
def add_wallet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Wallet.objects.create(
            user=request.user,
            name=name
        )
        return redirect('home')
    return render(request, 'add_wallet.html')

@login_required
def read_wallet(request):
    wallets = Wallet.objects.filter(user=request.user)
    return render(request, 'read_wallet.html',{'wallets': wallets})



@login_required
def update_wallet(request, id):
    wallet = Wallet.objects.get(id=id)
    if request.method == 'POST':
        wallet.name = request.POST.get('name')
        wallet.save()
        return redirect('read_wallet')
    return render(request, 'update_wallet.html', {'wallet': wallet})



@login_required
def delete_wallet(request, id):
    wallet = Wallet.objects.get(id=id)
    wallet.delete()
    return redirect('read_wallet')


@login_required
def deposit(request):
    if request.method == 'POST':
        wallet = Wallet.objects.get(id=request.POST.get('wallet'))
        amount = int(request.POST.get('amount'))
        wallet.balance += amount
        wallet.save()
        return redirect('home')
    wallets = Wallet.objects.filter(user=request.user)
    return render(request, 'deposit.html', {'wallets': wallets})



@login_required
def withdraw(request):
    if request.method == 'POST':
        wallet = Wallet.objects.get(id=request.POST.get('wallet'))
        amount = int(request.POST.get('amount'))
        if wallet.balance >= amount:
            wallet.balance -= amount
            wallet.save()
        return redirect('home')
    wallets = Wallet.objects.filter(user=request.user)
    return render(request, 'withdraw.html', {'wallets': wallets})

@login_required
def add_history(request):
    if request.method == 'POST':
        History.objects.create(
            wallet_id=request.POST.get('wallet'),
            category_id=request.POST.get('category'),
            title=request.POST.get('title'),
            amount=request.POST.get('amount'),
            type=request.POST.get('type'))
        return redirect('read_history')
    return render(request, 'add_history.html', {
        'wallets': Wallet.objects.filter(user=request.user), 'categories': Category.objects.all()})


@login_required
def read_history(request):
    history = History.objects.filter(wallet__user=request.user)
    return render(request, 'read_history.html',{'history': history})

@login_required
def update_history(request, id):
    history = History.objects.get(id=id)
    if request.method == 'POST':
        history.title = request.POST.get('title')
        history.amount = request.POST.get('amount')
        history.save()
        return redirect('read_history')
    return render(request, 'update_history.html', {'history': history})

@login_required
def delete_history(request, id):
    history = History.objects.get(id=id)
    history.delete()
    return redirect('read_history')


@login_required
def add_category(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST.get('name'))
        return redirect('see_category')
    return render(request, 'add_category.html')


@login_required
def see_category(request):
    categories = Category.objects.all()
    return render(request, 'see_category.html', {'categories': categories})


@login_required
def update_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.save()
        return redirect('see_category')
    return render(request, 'update_category.html', {'category': category})



@login_required
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('see_category')