# Konstanta
GOLDEN_RATIO = 1.61803

# Geometri
# Fungsi untuk menghitung luas dan keliling segitiga sama sisi
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(sisi):
    return 3 * sisi

# Fungsi untuk menghitung luas dan keliling jajar genjang
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def keliling_jajar_genjang(alas, sisi_miring):
    return 2 * (alas + sisi_miring)

# Fungsi untuk menghitung luas dan keliling trapesium sama kaki
def luas_trapesium(a, b, tinggi):
    return 0.5 * (a + b) * tinggi

def keliling_trapesium(a, b, sisi_miring):
    return a + b + 2 * sisi_miring

# Konversi suhu Reamur ke Celsius dan Fahrenheit ke Kelvin
def reamur_ke_celsius(r):
    return r * 1.25

def fahrenheit_ke_kelvin(f):
    return (f - 32) * 5/9 + 273.15
