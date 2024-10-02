from django.urls import path
from . import views
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),  # Halaman untuk index.html
    path('about-us/', views.about_us, name='about_us'),  # Halaman untuk about_us.html
    path('create-product/', views.create_product, name='create_product'),  # Halaman untuk form create_product
    path('products/', views.show_products, name='show_products'),  # Halaman untuk daftar produk
    path('products/json/', views.show_json, name='show_json'),  # URL untuk menampilkan data produk dalam format JSON
    path('products/xml/', views.show_xml, name='show_xml'),  # URL untuk menampilkan data produk dalam format XML
    path('products/json/<str:id>/', views.show_json_by_id, name='show_json_by_id'),  # URL untuk menampilkan produk dalam format JSON berdasarkan ID
    path('products/xml/<str:id>/', views.show_xml_by_id, name='show_xml_by_id'),  # URL untuk menampilkan produk dalam format XML berdasarkan ID
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('my_account/', views.my_account, name='my_account'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat

]
