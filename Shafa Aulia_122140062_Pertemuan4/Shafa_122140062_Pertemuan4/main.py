# Import seluruh modul
import math_operations
# Import fungsi tertentu
from math_operations import reamur_ke_celsius, fahrenheit_ke_kelvin

def menu():
    print("\n=== Kalkulator Matematika dan Konversi Suhu ===")
    print("1. Luas & Keliling Segitiga Sama Sisi")
    print("2. Luas & Keliling Jajar Genjang")
    print("3. Luas & Keliling Trapesium Sama Kaki")
    print("4. Konversi Suhu Reamur ke Celsius")
    print("5. Konversi Suhu Fahrenheit ke Kelvin")
    print("6. Tampilkan Konstanta GOLDEN_RATIO")
    print("0. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu (0-6): ")

    if pilihan == "1":
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        sisi = float(input("Masukkan panjang sisi segitiga: "))
        print(f"Luas segitiga: {math_operations.luas_segitiga(alas, tinggi)}")
        print(f"Keliling segitiga: {math_operations.keliling_segitiga(sisi)}")
    elif pilihan == "2":
        alas = float(input("Masukkan panjang alas jajar genjang: "))
        tinggi = float(input("Masukkan tinggi jajar genjang: "))
        sisi_miring = float(input("Masukkan panjang sisi miring: "))
        print(f"Luas jajar genjang: {math_operations.luas_jajar_genjang(alas, tinggi)}")
        print(f"Keliling jajar genjang: {math_operations.keliling_jajar_genjang(alas, sisi_miring)}")
    elif pilihan == "3":
        a = float(input("Masukkan sisi atas trapesium: "))
        b = float(input("Masukkan sisi bawah trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        sisi_miring = float(input("Masukkan panjang sisi miring trapesium: "))
        print(f"Luas trapesium: {math_operations.luas_trapesium(a, b, tinggi)}")
        print(f"Keliling trapesium: {math_operations.keliling_trapesium(a, b, sisi_miring)}")
    elif pilihan == "4":
        r = float(input("Masukkan suhu dalam Reamur: "))
        print(f"{r}°R = {reamur_ke_celsius(r):.2f}°C")
    elif pilihan == "5":
        f = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_ke_kelvin(f):.2f}K")
    elif pilihan == "6":
        print(f"Konstanta GOLDEN_RATIO dari modul: {math_operations.GOLDEN_RATIO}")
    elif pilihan == "0":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
