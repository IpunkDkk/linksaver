from django.shortcuts import render , redirect
from app.form import FormSaver
from django.contrib import messages
from app.models import Saver
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.





@login_required(login_url = settings.LOGGIN_URL)
def hapus_link(request , id_link):
    saver = Saver.objects.filter(id = id_link)
    saver.delete()
    messages.success(request , 'Link Berhasil DIhapus')
    return redirect('list-link')


@login_required(login_url = settings.LOGGIN_URL)
def editlink(request, id_link):
    saver = Saver.objects.get(id=id_link)
    template = "edit-link.html"
    if request.POST:
        form = FormSaver(request.POST , instance=saver)
        if form.is_valid():
            form.save()
            messages.success(request, 'data berhasil Diubah')
            return redirect('edit-link', id_link=id_link)
    else:
        form = FormSaver(instance=saver)
        konteks = {
            'form':form,
            'saver':saver
        }
        return render(request , template , konteks)




def home(request):
    return render(request , 'home.html')



@login_required(login_url = settings.LOGGIN_URL)
def linkview(request):
    saver = Saver.objects.all()
    judul = "list link"
    konteks = {
        'saver':saver,
        'judl':judul
    }
    return render(request , 'daftar-link.html' , konteks)

@login_required(login_url = settings.LOGGIN_URL)
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