from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def receipes(request):
    receipe_data = Receipe.objects.all()

    if request.GET.get("search_rec"):
        search_rec = request.GET.get("search_rec")
        print(f"=====search_rec======={search_rec}")
        receipe_data = receipe_data.filter(receipe_name__icontains = search_rec)

    context = {
        'page': 'Receipes Home',
        'receipe_data': receipe_data[::-1],
    }
    return render(request, 'receipes.html', context=context)

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

        return redirect('/receipes/add/')
    
    return render(request, 'receipe_add.html', context=context)

def receipe_delete(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()

    return redirect("/")

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