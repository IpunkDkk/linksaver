from django.shortcuts import render , redirect
from app.form import FormSaver
from django.contrib import messages
from app.models import Saver

# Create your views here.


def home(request):
    return render(request , 'home.html')

def linkview(request):
    saver = Saver.objects.all()
    judul = "list link"
    konteks = {
        'saver':saver,
        'judl':judul
    }
    return render(request , 'daftar-link.html' , konteks)


def tambahlink(request):
    if request.POST:
        form = FormSaver(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            form = FormSaver()
            konteks = {
                'form' : form
            }
            messages.success(request , 'Data Berhasil Ditambahkan')
            return render(request , 'tambah-link.html' , konteks)
    else:
        form = FormSaver()
        konteks = {
            'form':form
        }
    return render(request , 'tambah-link.html' ,konteks)