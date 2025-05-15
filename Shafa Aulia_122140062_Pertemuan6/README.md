# Tugas Praktikum 6: Manajemen Matakuliah

**Nama:** Shafa Aulia  
**NIM:** 122140062  
**Praktikum:** 6  

---

## Deskripsi

Aplikasi ini adalah sistem sederhana untuk manajemen data matkul menggunakan framework **Pyramid (Python)** dan **PostgreSQL** sebagai database.
Fitur utama mencakup **CRUD** (Create, Read, Update, Delete) data matkul yang dapat diakses melalui API maupun tampilan web berbasis **Jinja2**.

---

## Fitur

- Menampilkan daftar matkul lengkap  
- Menambah matkul baru  
- Mengubah data matkul  
- Menghapus matkul  

---

## Contoh Tampilan Aplikasi

![Tampilan awal](dokum/Screenshot%20(99).png)
Tampilan awal dari aplikasi yang berisikan beberapa matkul yang sudah diinputkan sebelumnya.

![Tambah Matkul](dokum/Screenshot%20(101).png)
![Tambah Matkul](dokum/Screenshot%20(102).png)
Menambah matkul menggunakan fungsi yang ada di web dan akan terintegritas dengan database yang telah dibuat di postgreSQL.


![Apus Matkul](dokum/Screenshot%20(103).png)
![Apus Matkul](dokum/Screenshot%20(104).png)
Menghapus matkul menggunakan fungsi yang ada di web dan akan terintegritas dengan database yang telah dibuat di postgreSQL.

---

## Cara Menjalankan

1. Pastikan environment Python sudah aktif (virtualenv)  
2. Jalankan server dengan perintah:

   ```bash
   pserve development.ini --reload
