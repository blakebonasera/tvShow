from django.shortcuts import render, HttpResponse, redirect
from .models import Tv

def index(request):
    return redirect("/shows")

def show(request):
    context = {
        'all_tv': Tv.objects.all()
    }
    return render(request, 'show.html', context)

def makeShow(request):
    return render(request, 'newshow.html')

def newShow(request):
    title = request.POST['title']
    network = request.POST['network']
    release = request.POST['release']
    desc = request.POST['description']
    Tv.objects.create(
        title=title,
        network=network,
        release=release,
        desc=desc
    )
    return redirect('/shows')

def update(request, num):
    update_tv = Tv.objects.get(id=num)
    updated_title = request.POST['title']
    updated_network = request.POST['network']
    updated_release = request.POST['release']
    updated_desc = request.POST['description']
    update_tv.title = updated_title
    update_tv.network = updated_network
    update_tv.release = updated_release
    update_tv.desc = updated_desc
    update_tv.save()
    return redirect('/shows')

def edit(request, num):
    context ={
        'all_tv': Tv.objects.all()
    }
    Tv.objects.get(id=num)
    return render(request, 'update.html', context)

def delete(request, num):
    delete = Tv.objects.get(id=num)
    delete.delete()
    return redirect("/")

def info(request, num):
    Tv.objects.get(id=num)
    context = {
        'show_tv': Tv.objects.get(id=num),
        'all_tv': Tv.objects.all()
    }
    return render(request,'showinfo.html', context)