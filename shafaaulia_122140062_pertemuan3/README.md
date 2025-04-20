## Nama : Shafa Aulia
## NIM : 122140062
## Praktikum Pemweb Minggu ke-3
--- 
# Shafa's Mini Library
Shafa's Mini Library merupakan tugas praktikum minggu ke-3 untuk matakuliah pemweb. Shafa's Mini Library adalah aplikasi manajemen koleksi buku pribadi basis web yang dibuat menggunakan React js dasar 
Aplikasi ini biasa untuk mencatat buku yang dimiliki, sedang dibaca, atau ingin dibeli
Selain itu user juga bisa memfilter, mencari, menambahkan, mengedit, dan menghapus data buku yang dimilikinya. 

## Instalisasi Library 
![Install Screenshot](src\assets\screenshots\Instalisasi.png)

## Fitur

- Tambah/Edit/Hapus data
- Filter dan pencarian data buku
- Penyimpanan dengan localStorage
- Tampilan responsif dan bersih
---

## Fitur React yang Digunakan
Aplikasi ini dibangun menggunakan pendekatan modern React dengan fitur-fitur sebagai berikut:

- Functional Components & Hooks
Seluruh komponen ditulis sebagai functional component menggunakan Hooks seperti useState dan useEffect untuk mengelola state dan side effect.

- Context API
Digunakan untuk menyimpan dan membagikan state global books ke seluruh komponen melalui BookContext.

- Custom Hooks
Dua custom hooks (useFilterAndSearch, useBookStats, dan useLocalStorage) dibuat untuk memisahkan logika filter dan pencarian dari komponen utama.

- React Router
Navigasi antar halaman Home (/) dan Daftar buku (/stats) dikelola menggunakan react-router-dom.

- LocalStorage
Data buku tersimpan secara lokal di browser menggunakan localStorage, sehingga tetap ada meskipun halaman di-refresh.

- PropTypes
Setiap komponen menggunakan PropTypes untuk validasi props yang diterima.

- Reusable Components
Komponen seperti BookForm, SearchBar, BookFilter, dan BookList dibuat reusable dan modular.

- Error Handling Form
Validasi input form dilakukan untuk memastikan semua data diisi dengan benar sebelum ditambahkan atau diperbarui.
---

## Screenshot

### Halaman Home
gambar dibawah merupakan tampilan website yang dibuat yaitu Shafa's Mini Library. Pada website dapat dilakukan beberapa aktivitas diantaranya menambahkan, menghapus, dan melihat daftar buku yang diinputkan. Selain itu terdapat fitur filter buku, dan juga edit keterangan buku.
![Home Screenshot](src\assets\screenshots\Home.png)

### List
gambar dibawah merupakan tampilan jika user sudah menginputkan daftar buku yang dimilikinya.
![List Screenshot](src\assets\screenshots\List.png) 

### Error
gambar dibawah merupakan tampilan error ketika user ingin menginputkan buku namun data yang diinputkan tidak lengkap.
![Error Screenshot](src\assets\screenshots\Error.png)

### Book list Page
gambar dibawah merupakan tampilan pada page daftar buku yang berisi kumpulan buku yang diinputkan user.
![ListPage Screenshot](src\assets\screenshots\BookListPage.png)

### Penggunaan FilterBook
gambar dibawah merupakan implementasi dari fitur filter book berdasarkan semua buku yang diinput, buku yang dimiliki, buku yang sedang dibaca, dan buku yang akan dibeli. 
![Semua Screenshot](src\assets\screenshots\List.png)
![Beli Screenshot](src\assets\screenshots\FilterBeli.png)
![Dibaca Screenshot](src\assets\screenshots\FilterDibaca.png)

### Penggunaan Fitur Search
![Fitur Search Screenshot](src\assets\screenshots\fitursearch.png)

## Hasil Testing 
berikut hasil testing 
![Testing Screenshot](src\assets\screenshots\Testing.png)

## Instalasi

1. Clone repositori:
   ```bash
   git clone https://github.com/shaaapaa/shafaaulia_122140062_pertemuan3.git
   cd shafaaulia_122140062_pertemuan3
