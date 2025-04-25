# Modul matematika sederhana

# Variabel dalam modul
pi = 3.14159

# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(radius):
    return pi * radius * radius

# Fungsi untuk menghitung keliling lingkaran
def hitung_keliling_lingkaran(radius):
    return 2 * pi * radius

# Fungsi untuk mengkonversi suhu dari Celsius ke Fahrenheit
def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Fungsi untuk mengkonversi suhu dari Fahrenheit ke Celsius
def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Mengimpor modul yang telah kita buat
import my_module

# Menggunakan variabel dari modul
print(f"Nilai Pi: {my_module.pi}")

# Menggunakan fungsi dari modul
radius = 5
luas = my_module.hitung_luas_lingkaran(radius)
keliling = my_module.hitung_keliling_lingkaran(radius)

print(f"Lingkaran dengan radius {radius}")
print(f"Luas: {luas:.2f}")
print(f"Keliling: {keliling:.2f}")

# Mengimpor fungsi tertentu dari modul
from my_module import celsius_ke_fahrenheit, fahrenheit_ke_celsius

# Menggunakan fungsi yang diimpor
celsius = 25
fahrenheit = celsius_ke_fahrenheit(celsius)
print(f"\n{celsius}°C = {fahrenheit:.2f}°F")

fahrenheit = 98.6
celsius = fahrenheit_ke_celsius(fahrenheit)
print(f"{fahrenheit}°F = {celsius:.2f}°C")

# Mengimpor semua dari modul (umumnya tidak disarankan)
# from my_module import *

# Mengimpor modul dengan alias
import my_module as mm
print(f"\nMenggunakan alias: Pi = {mm.pi}")

# Menggunakan modul bawaan Python
import math
import random
import datetime
import os

# Menggunakan math module
print("Modul math:")
print(f"Nilai Pi: {math.pi}")
print(f"Akar kuadrat dari 16: {math.sqrt(16)}")
print(f"Cos(0): {math.cos(0)}\n")

# Menggunakan random module
print("Modul random:")
print(f"Angka acak antara 1 dan 10: {random.randint(1, 10)}")
print(f"Pilihan acak dari list: {random.choice(['apel', 'jeruk', 'mangga'])}\n")

# Menggunakan datetime module
print("Modul datetime:")
today = datetime.datetime.now()
print(f"Tanggal dan waktu saat ini: {today}")
print(f"Hanya tanggal: {today.date()}")
print(f"Hanya waktu: {today.time()}\n")

# Menggunakan os module
print("Modul os:")
print(f"Direktori saat ini: {os.getcwd()}")
print(f"List file dalam direktori: {os.listdir()[:5]}")  # Menampilkan 5 item pertama
