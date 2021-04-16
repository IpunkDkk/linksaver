from django.contrib import admin
from django.urls import path
from app.views import home , tambahlink , linkview , editlink , hapus_link
from django.contrib.auth.views import LoginView , LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home , name=''),
    path('tambah-link/', tambahlink , name='tambah-link'),
    path('list-link/' , linkview , name='list-link'),
    path('edit-link/<int:id_link>' , editlink , name='edit-link'),
    path('hapus-link/<int:id_link>' , hapus_link , name='hapus-link'),
    path('login/', LoginView.as_view() , name='login'),
    path('logout/' , LogoutView.as_view(next_page='login') , name='logout')
]
