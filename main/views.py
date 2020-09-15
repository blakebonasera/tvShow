from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
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
    errors = Tv.objects.validate(request.POST)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
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
        messages.success(request, 'You made a new show??? Did you call Netflix first???')
        return redirect('/shows')

def update(request, num):
    errors = Tv.objects.validate(request.POST)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/<int:num>/edit')
    else:
        update_tv = Tv.objects.get(id=num)
        update_tv.title = request.POST['title']
        update_tv.network = request.POST['network']
        update_tv.release = request.POST['release']
        update_tv.desc = request.POST['description']
        update_tv.save()
        messages.success(request, "Look at you! YOU KNOW SOMETHING!")
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