Implementasi Checklist Tugas

Membuat Proyek Django Baru (sudah)
    - Saya membuat dengan perintah django-admin startproject aura_artisan

Membuat Aplikasi Baru Bernama main (sudah)
    - cd <nama proyek>
    python manage.py startapp main

Melakukan Routing pada Proyek (sudah)
    -  Buka file myproject/urls.py dan tambahkan path untuk aplikasi main

Membuat Model Product pada Aplikasi main (sudah)
    - Buka file main/models.py dan tambahkan model Product dengan atribut name, price, dan description
    - Setelah itu saya menjalankan perintah python manage.py makemigrations & python manage.py migrate

Membuat Fungsi pada views.py (sudah)
    - Saya membuat Sebuah fungsi view yang menerima request sebagai parameter.
    - Menggunakan render() untuk merender template index.html yang akan dikirim kembali ke klien sebagai respons.

Membuat Routing pada urls.py di Aplikasi main (sudah)
    - Buat file urls.py di direktori main (jika belum ada) dan tambahkan routing untuk memetakan fungsi di views.py

Melakukan deployment ke PWS 
    - Pada settings.py tambahkan url deployment pws pada Allowed_HOSTS
    - lalu lakukan git remote add pws 
    - ubah branch ke master dan lakukan git push pws master

http://muhammad-fadhil38-auraartisanweb.pbp.cs.ui.ac.id/


Jawaban Pertanyaan pada README.md

Implementasi Checklist Secara Step-by-Step:
sudah dijawab di atas

Bagan Request Client ke Web Aplikasi Django:

Client Request -> urls.py -> views.py -> models.py -> templates (HTML) -> Response ke Client
Penjelasan Bagan:
    urls.py: Menerima request dan memetakan ke fungsi view yang sesuai.
    views.py: Mengolah logika, mengambil data dari model, dan menyiapkan context untuk template.
    models.py: Berisi definisi model (seperti Product) dan menghubungkan dengan database.
    Templates (HTML): Menampilkan data dari views.py kepada pengguna.

Fungsi Git dalam Pengembangan Perangkat Lunak:
    Git digunakan untuk version control, memungkinkan pengembang melacak perubahan kode, bekerja secara kolaboratif, mengelola branch, dan mengintegrasikan perubahan dengan mudah.

Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak:
    Django adalah framework yang menyediakan banyak fitur bawaan seperti ORM, form handling, dan keamanan. Ini memudahkan pemula belajar konsep-konsep dasar web development sambil menggunakan alat yang kuat dan praktis.


Mengapa Model pada Django Disebut Sebagai ORM?
    ORM (Object-Relational Mapping) adalah teknik untuk menghubungkan atau memetakan model objek di kode dengan tabel-tabel dalam database. Django ORM memungkinkan pengembang bekerja dengan database menggunakan kode Python alih-alih SQL, membuat pengelolaan data menjadi lebih efisien.
    


