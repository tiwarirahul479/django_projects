from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def receipes(request):
    receipe_data = Receipe.objects.all()
    search_rec = ''

    if request.GET.get("search_rec"):
        search_rec = request.GET.get("search_rec")
        receipe_data = receipe_data.filter(receipe_name__icontains = search_rec)

    receipe_data = receipe_data[::-1]

    paginator = Paginator(receipe_data, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page': 'Receipes Home',
        'receipe_data': page_obj,
        'search_rec': search_rec,
    }
    return render(request, 'receipes.html', context=context)

@login_required(login_url="/login")
def receipe_add(request):
    context = {
        'page': 'Add Receipes',
    }
    if request.method == 'POST':
        data = request.POST

        receipe_name = data['receipe_name']
        receipe_description = data['receipe_description']
        receipe_image = request.FILES['receipe_image']

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        messages.success(request, "Receipe Added successfully!")

        return redirect('/receipes/add/')
    
    return render(request, 'receipe_add.html', context=context)

@login_required(login_url="/login")
def receipe_delete(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()

    return redirect("/")

@login_required(login_url="/login")
def receipe_update(request, id):
    queryset = Receipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST

        queryset.receipe_name = data['receipe_name']
        queryset.receipe_description = data['receipe_description']
        if request.FILES.get('receipe_image'):
            queryset.receipe_image = request.FILES['receipe_image']

        queryset.save()

        return redirect('/')

    context = {
        'recepie_update': queryset,
    }

    return render(request, 'receipe_update.html', context=context)

def receipe_open(request, id):
    queryset = Receipe.objects.get(id = id)
    context = {
        'recepie_data': queryset,
    }

    return render(request, 'receipe_open_page.html', context=context)

def login_page(request):
    context = {
        'page': "Login"
    }

    if request.method == 'POST':
        data = request.POST

        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request, "Username doesn't exist!")
            return redirect("/login")
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid password!")
            return redirect("/login")
        else:
            login(request, user=user)
            redirect_url = "/"
            if request.GET.get("next"):
                redirect_url = request.GET.get("next")
            return redirect(redirect_url)

    return render(request, 'login.html', context=context)

def logout_page(request):
    logout(request)
    return redirect("/login")

def register_page(request):
    context = {
        'page': "Register"
    }

    if request.method == 'POST':
        data = request.POST

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already exist!")
            return redirect("/register")
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        login(request, user=user)
        messages.success(request, "User register successfully!")

        return redirect("/")

    return render(request, 'register.html', context=context)