# Library Management System

## Overview

Shafa's Management Perpus adalah aplikasi desktop sederhana yang dikembangkan dengan Python dan Tkinter. Aplikasi ini memanfaatkan konsep Object-Oriented Programming (OOP) seperti abstract class, inheritance, encapsulation, dan polymorphism untuk mengelola koleksi item perpustakaan.

## Fitur Utama

* **Tambah Item**: Menambahkan buku (`Book`) dan koran (`Newspaper`) ke perpustakaan.
* **Daftar Item**: Menampilkan semua item yang tersedia dalam tabel interaktif.
* **Pencarian**: Mencari item berdasarkan judul atau ID.
   ```
## Penjelasan Kode

### 1. `LibraryItem` (Abstract Class)

`
LibraryItem` adalah abstract class yang menjadi dasar untuk semua item perpustakaan. isinya terdiri dari 

* Atribut private `__id` untuk identifikasi unik.
* Atribut protected `_title` sebagai judul item.
* Method abstract `get_info()` yang wajib di-override oleh subclass.
* Property decorator untuk `id` dan `title`.

### 2. Subclasses: `Book` dan `Newspaper`

* **Book**: Menyimpan `author` dan `pages`, mengimplementasikan `get_info()` untuk menampilkan detail buku.
* **Newspaper**: Menyimpan `publish_date` dan `publisher`, menggunakan property decorator untuk `publish_date`, serta `get_info()` untuk menampilkan detail koran.

Kedua subclass memanfaatkan konsep **inheritance** dan **polymorphism** untuk mengoverride method abstract.

### 3. `Library` (Collection Manager)

Class ini mengelola koleksi item perpustakaan:

* Atribut protected `_items` menyimpan list objek `LibraryItem`.
* `add_item(item)`: Menambahkan item baru.
* `list_items()`: Mengembalikan daftar tuple detail semua item.
* `search(query)`: Mencari item berdasarkan judul atau ID.