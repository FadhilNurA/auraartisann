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
    







========================================================================================================================================





Berikut adalah langkah-langkah implementasi checklist ini:

    Membuat form input untuk menambahkan produk dengan menggunakan create_product dan menghubungkannya dengan model show_product.

    Menambahkan empat fungsi views baru (show_json, show_xml, show_json_by_id, show_xml_by_id) untuk menampilkan data produk dalam format JSON dan XML, serta memfilter berdasarkan ID jika diperlukan. 

def show_products(request):
    products = Product.objects.all()  # Mengambil semua entri produk dari database
    context = {'products': products}
    return render(request, "products.html", context)  # Mengarahkan ke template "products.html"

def show_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type='application/json')

def show_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products) 

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    Menambahkan routing URL untuk masing-masing view yang telah dibuat agar bisa diakses melalui URL yang sesuai. Routing URL sangat penting untuk menentukan endpoint yang dapat diakses oleh pengguna. 
    
    path('products/json/', views.show_json, name='show_json'),  # URL untuk menampilkan data produk dalam format JSON
    path('products/xml/', views.show_xml, name='show_xml'),  # URL untuk menampilkan data produk dalam format XML
    path('products/json/<str:id>/', views.show_json_by_id, name='show_json_by_id'),  # URL untuk menampilkan produk dalam format JSON berdasarkan ID
    path('products/xml/<str:id>/', views.show_xml_by_id, name='show_xml_by_id'),  # URL untuk menampilkan produk dalam format XML berdasarkan ID

    Setelah semua routing URL dan views selesai dibuat, kita bisa menguji setiap endpoint menggunakan Postman. Berikut langkah-langkahnya:

    GET http://localhost:8000/products/json/ – Menampilkan semua produk dalam format JSON.
    GET http://localhost:8000/products/xml/ – Menampilkan semua produk dalam format XML.
    GET http://localhost:8000/products/json/1/ – Menampilkan produk dengan ID 1 dalam format JSON. (id hanya contoh)
    GET http://localhost:8000/products/xml/1/ – Menampilkan produk dengan ID 1 dalam format XML. (id hanya contoh)


Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Pengiriman data (data delivery) sangat penting dalam pengimplementasian platform karena memungkinkan aplikasi untuk bertukar informasi secara efisien antara klien dan server. Tanpa pengiriman data, aplikasi tidak dapat berfungsi dengan baik dalam hal mendapatkan, menambahkan, atau memperbarui informasi di server. Selain itu, data delivery juga memastikan bahwa data yang ditampilkan selalu up-to-date dan sinkron antara berbagai perangkat dan pengguna.

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya mungkin JSON lebih baik untuk banyak aplikasi web modern dibandingkan XML karena beberapa alasan:
    Lebih ringan: JSON menggunakan sintaks yang lebih sederhana dan lebih ringkas dibandingkan XML.
    Lebih cepat: Karena ukurannya yang lebih kecil, JSON lebih cepat dikirim dan diproses.
    Kemudahan parsing: JSON mudah di-parse (dibaca dan dikonversi menjadi objek) dalam bahasa pemrograman modern seperti JavaScript, Python, dll.

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dikirimkan melalui form memenuhi aturan validasi yang telah ditentukan di form tersebut. Jika data memenuhi semua kriteria validasi (misalnya tipe data yang benar, tidak kosong, dll.), method ini akan mengembalikan nilai True, dan jika ada kesalahan validasi, method ini akan mengembalikan False. Kita membutuhkan method ini untuk memastikan bahwa hanya data yang valid yang akan diproses dan disimpan ke dalam database, sehingga menghindari terjadinya error dan memastikan integritas data.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token digunakan untuk melindungi aplikasi Django dari serangan CSRF (Cross-Site Request Forgery). Token ini adalah sebuah nilai acak yang ditambahkan pada setiap form dan divalidasi oleh server saat form dikirimkan. Jika csrf_token tidak ada, penyerang dapat mengirimkan permintaan yang berbahaya (seolah-olah dari pengguna yang sah) dan memanipulasi data di server tanpa sepengetahuan pengguna. Tanpa csrf_token, aplikasi akan rentan terhadap serangan ini, di mana penyerang dapat menjalankan tindakan tidak sah seperti mengubah data pengguna atau menambahkan data tanpa izin.


screenshot:

XML
![alt_text](https://github.com/FadhilNurA/auraartisann/blob/main/gambar/xml.png?raw=true)


JSON
![alt_text](https://github.com/FadhilNurA/auraartisann/blob/main/gambar/json.png?raw=true)



XML by Id
![alt_text](https://github.com/FadhilNurA/auraartisann/blob/main/gambar/xml_show_id.png?raw=true)



Json by Id
![alt_text](?raw=true)




========================================================================================================================================

Tugas 4

1. Mengimplementasikan Fungsi Registrasi, Login, dan Logout
Langkah-langkah:

Registrasi:

Buat register.html dengan form untuk username, password, dan confirm password.
Tambahkan view register untuk menangani registrasi pengguna baru.
Gunakan UserCreationForm atau buat form sendiri untuk registrasi.
Pada form valid, simpan user dan redirect ke halaman login atau halaman utama.

Login:

Buat login.html dengan form untuk username dan password.
Tambahkan view login menggunakan authenticate dan login dari Django.
Set cookie last_login saat user berhasil login.

Logout:

Tambahkan view logout menggunakan logout dari Django.
Redirect pengguna ke halaman login setelah logout.

2. Membuat Dua Akun Pengguna dengan Tiga Dummy Data
Langkah-langkah:
Buat dua akun pengguna melalui halaman registrasi atau shell Django.

Buat tiga dummy data untuk setiap akun menggunakan model Product yang terhubung ke User.

Dummy 1:
muhammad.fadhil38
Fadhil0912

Product List
gedagedigedagedao - 1000 - 1 available
gedagedigedagedao - 1000 - 1 available
gedagedigedagedao - 1000 - 1 available
ei ei ei - 1000 - 3 available


Dummy 2:
furina.123
Admin#1234

Product List
Test2-1 - 1 - 100 available
Test2-2 - 1000 - 1 available
Test2-3 - 10000 - 1 available

3. Menghubungkan Model Product dengan User
Langkah-langkah:
Pastikan model Product memiliki field user sebagai ForeignKey.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

Saat menyimpan Product melalui form, pastikan untuk menetapkan user.
    product = form.save(commit=False)
    product.user = request.user
    product.save()

4. Menampilkan Detail Informasi Pengguna yang Logged In
Ubah my_account.html untuk menampilkan detail informasi pengguna seperti username dan last_login.
<p>Hello, {{ name }}!</p>
<h5>Sesi terakhir login: {{ last_login }}</h5>

Pastikan views.py mengirim context name dan last_login.

def my_account(request):
    context = {
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, 'my_account.html', context)

5. Menjawab Pertanyaan di README.md

Perbedaan antara HttpResponseRedirect() dan redirect():
HttpResponseRedirect: Kelas yang menghasilkan respons redirect dengan status HTTP 302. Memerlukan URL secara eksplisit.
redirect(): Shortcut yang menerima argumen URL atau nama view dan mengembalikan HttpResponseRedirect.

Cara Kerja Penghubungan Model Product dengan User:
Menggunakan ForeignKey di Product untuk mereferensikan User. Setiap Product akan terhubung ke satu user tertentu.

Perbedaan authentication dan authorization:
Authentication: Proses verifikasi identitas pengguna (misalnya, login).
Authorization: Proses menentukan hak akses pengguna terhadap sumber daya tertentu setelah pengguna terverifikasi.

Bagaimana Django Mengimplementasikan Authentication dan Authorization?:
Authentication dilakukan melalui backend autentikasi seperti authenticate() dan login().
Authorization dilakukan menggunakan permission dan decorator seperti @login_required.\

Bagaimana Django Mengingat Pengguna yang Telah Login?:
Django menggunakan session yang disimpan di cookies untuk mengingat pengguna yang login. Cookies juga digunakan untuk menyimpan data seperti last_login.


========================================================================================================================================

Tugas 5

1. Fungsi untuk Menghapus dan Mengedit Product:
Buat fungsi untuk menghapus dan mengedit produk di views.py. Pastikan kita menghubungkan form ke produk yang benar menggunakan ID produk.
Tambahkan URL routing yang sesuai di urls.py untuk mengarahkan ke fungsi edit dan delete.

2. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework
Struktur Grid dan Flex: Saya menggunakan flex dan justify-center untuk memusatkan form login secara vertikal dan horizontal. Kelas seperti min-h-screen membantu menjaga halaman tetap proporsional sesuai dengan ukuran layar perangkat yang berbeda.

Penggunaan Border dan Shadow: Untuk mempercantik form login dll, saya menambahkan border, rounded-lg, dan shadow-md yang memberikan tampilan modern dengan sudut tumpul dan bayangan halus.

Input Fields: Setiap elemen input (username dan password) dibuat menggunakan kelas Tailwind seperti rounded-md, border, dan focus:outline-none agar form terlihat minimalis namun tetap elegan.

{% for product in products %}: Saya menggunakan loop ini untuk menampilkan setiap produk yang ada dalam variabel products, yang merupakan queryset dari model produk yang diteruskan dari views.

{% empty %}: Ini adalah template tag khusus di Django. Jika tidak ada produk dalam queryset products, kode di dalam {% empty %} akan dijalankan, yang dalam hal ini menampilkan pesan bahwa tidak ada produk yang terdaftar beserta gambar ilustrasi.

Jika produk terdaftar di aplikasi, halaman akan menampilkan produk-produk tersebut dalam bentuk card yang diatur dengan tampilan yang responsif:

Card Layout: Setiap produk ditampilkan dalam div yang berkelas bg-white rounded-lg shadow-lg p-4, memberikan tampilan elegan dan terstruktur untuk masing-masing produk. Detail seperti nama produk, harga, dan stok ditampilkan dalam <h2> dan <p>

Tombol Edit dan Delete: Setiap card produk dilengkapi dengan dua tombol aksi, yaitu untuk mengedit dan menghapus produk. 

3. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

Navbar dimulai dengan menampilkan nama aplikasi atau logo di sisi kiri yang di-link ke halaman utama (home) menggunakan tag <a>. Pada layar kecil dan besar, elemen ini tetap terlihat.

Pada layar besar (desktop), navigasi yang terlihat terdiri dari beberapa link seperti Home, New Arrival, About Us, dan kondisi khusus untuk Login atau My Account jika pengguna sudah login. Ada juga pengecekan untuk beberapa nama pengguna yang secara khusus memiliki akses ke halaman Products.

Ini diatur menggunakan Tailwind CSS class hidden md:flex, yang memastikan link hanya muncul di layar dengan ukuran medium (md) ke atas. Pada layar kecil (mobile), link ini tersembunyi dan akan digantikan dengan menu mobile.

Pada layar kecil, link di navbar akan disembunyikan dan sebagai gantinya muncul tombol hamburger (ikon tiga garis) di kanan navbar. Tombol ini diatur dengan md:hidden sehingga hanya terlihat di layar kecil.

Saat tombol hamburger diklik, menu mobile akan ditampilkan menggunakan JavaScript untuk menambah/menghapus class hidden.


Menjawab Pertanyaan

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Selektor Inline (ditulis langsung di elemen HTML menggunakan atribut style) memiliki prioritas tertinggi.
Selektor ID (#id) memiliki prioritas lebih tinggi dibandingkan selektor kelas atau tipe elemen.
Selektor Kelas (.class), Pseudo-class, dan Atribut memiliki prioritas sedang.
Selektor Elemen (seperti div, p, dll.) memiliki prioritas terendah. Jika ada beberapa selektor yang berkonflik, browser akan menerapkan yang memiliki prioritas lebih tinggi. Jika dua selektor memiliki tingkat specificity yang sama, selektor yang terakhir didefinisikan di CSS akan diterapkan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design memastikan bahwa tampilan aplikasi web dapat menyesuaikan dengan berbagai ukuran layar dan perangkat, mulai dari ponsel hingga desktop. Ini penting karena pengguna dapat mengakses aplikasi dari berbagai perangkat dengan ukuran layar berbeda. Tanpa desain yang responsif, pengguna mungkin kesulitan menavigasi aplikasi pada perangkat kecil. Contoh aplikasi yang sudah menerapkan responsive design adalah Google.com dan Facebook.com, sedangkan beberapa situs yang lebih lama atau aplikasi yang tidak dioptimalkan untuk mobile, seperti situs web lokal yang jarang diperbarui, mungkin belum menerapkan responsive design.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin: Ruang di luar border elemen. Ini menciptakan jarak antara elemen-elemen yang berbeda.
Contoh implementasi:
.element {
    margin: 20px;
}

Border: Garis yang mengelilingi elemen. Border terletak di antara margin dan padding.
Contoh implementasi:
.element {
    border: 2px solid black;
}

Padding: Ruang di dalam elemen, antara konten elemen dan border-nya.
Contoh implementasi:
.element {
    padding: 10px;
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox: Flexbox digunakan untuk menyusun elemen-elemen di dalam kontainer dengan cara yang fleksibel dan mudah diatur. Flexbox memungkinkan distribusi ruang secara efisien dan perataan elemen secara responsif dalam satu dimensi (baris atau kolom). 
Contoh implementasi:
.container {
    display: flex;
    justify-content: center;
    align-items: center;
}

Grid Layout: Grid digunakan untuk menyusun elemen-elemen dalam dua dimensi (baris dan kolom). Grid memberikan kontrol yang lebih kompleks untuk tata letak elemen yang lebih rumit. 
Contoh implementasi:
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
}

