from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Nama item
    price = models.IntegerField()            # Harga item
    description = models.TextField()         # Deskripsi item

    stock = models.IntegerField(default=0)   # Stok item
    category = models.CharField(max_length=255, blank=True)  # Kategori item
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Gambar item
    rating = models.FloatField(default=0.0)  # Rating item
    date_added = models.DateField(auto_now_add=True)  # Tanggal item ditambahkan

    def __str__(self):
        return f"{self.name} - {self.price}"

    @property
    def is_in_stock(self):
        return self.stock > 0
