from django.db import models
# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=20)
    keterangan = models.TextField()
    def __str__(self):
        return self.nama

class Saver(models.Model):
    judul = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    # cover = models.ImageField(upload_to='cover/' , null = True)
    tanggal = models.DateTimeField(auto_now_add=True , null = True)
    kategori_id = models.ForeignKey(Kategori , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.judul
