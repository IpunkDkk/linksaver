from django.contrib import admin
from app.models import Saver , Kategori

# Register your models here.
class SaverAdmin(admin.ModelAdmin):
    list_display = ['judul' , 'link' , 'tanggal' , 'kategori_id']



admin.site.register(Saver , SaverAdmin)
admin.site.register(Kategori)