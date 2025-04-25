# Program Python pertama
print("Hello, World!")
print("Selamat datang di praktikum Python")
print("Saya sedang belajar Python")

# Variabel dan tipe data dasar
nama = "Shafa Aulia"    # string
usia = 21               # integer
tinggi = 150            # float
is_mahasiswa = True      # boolean

# # Memeriksa tipe data
# print("\nTipe data variabel:")
# print("Tipe data nama:", type(nama))
# print("Tipe data usia:", type(usia))
# print("Tipe data tinggi:", type(tinggi))
# print("Tipe data is_mahasiswa:", type(is_mahasiswa))

# Konversi tipe data
# usia_str = str(usia)
# print("\nUsia (string):", usia_str)
# print("Tipe data usia_str:", type(usia_str))

# Input dari user
print("\nInput dari pengguna")
nama_input = input("Masukkan nama Anda: ")
usia_input = int(input("Masukkan usia Anda: "))  # konversi input ke integer
print(f"Halo {nama_input}, usia Anda {usia_input} tahun")

# Operator aritmatika
a = 10
b = 3

print("Operator Aritmatika:")
print("a + b =", a + b)    # Penjumlahan
print("a - b =", a - b)    # Pengurangan
print("a * b =", a * b)    # Perkalian
print("a / b =", a / b)    # Pembagian (hasil float)
print("a // b =", a // b)  # Pembagian bulat
print("a % b =", a % b)    # Modulo (sisa pembagian)
print("a ** b =", a ** b)  # Pangkat

# Operator perbandingan
print("\nOperator Perbandingan:")
print("a == b:", a == b)  # Sama dengan
print("a != b:", a != b)  # Tidak sama dengan
print("a > b:", a > b)    # Lebih besar dari
print("a < b:", a < b)    # Lebih kecil dari
print("a >= b:", a >= b)  # Lebih besar atau sama dengan
print("a <= b:", a <= b)  # Lebih kecil atau sama dengan

# Operator logika
x = True
y = False

print("\nOperator Logika:")
print("x and y:", x and y)  # AND
print("x or y:", x or y)    # OR
print("not x:", not x)      # NOT

# Operator assignment
c = 5
print("\nOperator Assignment:")
print("Nilai awal c =", c)
c += 3  # Sama dengan c = c + 3
print("Setelah c += 3, c =", c)
c -= 1  # Sama dengan c = c - 1
print("Setelah c -= 1, c =", c)
c *= 2  # Sama dengan c = c * 2
print("Setelah c *= 2, c =", c)
c /= 4  # Sama dengan c = c / 4
print("Setelah c /= 4, c =", c)

# Contoh if-else
nilai = int(input("Masukkan nilai (0-100): "))
grade = ""

# If-elif-else
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Nilai: {nilai}, Grade: {grade}")

# Keterangan kelulusan
if nilai >= 60:
    print("Status: LULUS")
else:
    print("Status: TIDAK LULUS")

# Nested if
print("\nKeterangan:")
if nilai >= 60:
    if nilai >= 90:
        print("Excellent!")
    elif nilai >= 80:
        print("Great job!")
    else:
        print("Good, keep improving!")
else:
    if nilai >= 40:
        print("Need more practice")
    else:
        print("Need serious attention")

# Ternary operator
status = "LULUS" if nilai >= 60 else "TIDAK LULUS"
print(f"Status (ternary): {status}")

# Multiple conditions
if nilai >= 80 and nilai <= 100:
    print("Nilai sangat baik")
elif nilai >= 60 or nilai == 55:
    print("Nilai cukup")
elif not (nilai < 40):
    print("Nilai di atas 40")

# For loop dengan range
print("For loop dengan range:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

# Range dengan start, stop, step
print("\nRange dengan start, stop, step:")
for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i, end=" ")
print()

# For loop dengan list
print("\nFor loop dengan list:")
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]
for item in buah:
    print(item)

# For loop dengan enumerate (mendapatkan indeks)
print("\nFor loop dengan enumerate:")
for index, item in enumerate(buah):
    print(f"Index {index}: {item}")

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print()

# While dengan break
print("\nWhile dengan break:")
angka = 0
while True:
    print(angka, end=" ")
    angka += 1
    if angka >= 5:
        break
print()

# For loop dengan continue
print("\nFor loop dengan continue:")
for i in range(10):
    if i % 2 == 0:  # Skip bilangan genap
        continue
    print(i, end=" ")
print()

# Nested loops
print("\nNested loops (multiplication table):")
for i in range(1, 5):
    for j in range(1, 5):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

# Loop dengan else
print("\nLoop dengan else:")
for i in range(5):
    print(i, end=" ")
else:
    print("Loop selesai")

# List comprehension - cara singkat untuk membuat list
print("\nList comprehension:")
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Fungsi dasar
def sapa():
    print("Halo, selamat datang!")

# Memanggil fungsi
print("Memanggil fungsi sapa():")
sapa()

# Fungsi dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat datang!")

print("\nFungsi dengan parameter:")
sapa_nama("Budi")
sapa_nama("Ani")

# Fungsi dengan parameter default
def sapa_lengkap(nama, pesan="Selamat datang!"):
    print(f"Halo, {nama}! {pesan}")

print("\nFungsi dengan parameter default:")
sapa_lengkap("Citra")
sapa_lengkap("Dodi", "Semoga harimu menyenangkan!")

# Fungsi dengan return value
def jumlah(a, b):
    return a + b

print("\nFungsi dengan return value:")
hasil = jumlah(5, 3)
print(f"5 + 3 = {hasil}")

# Fungsi dengan multiple return values
def operasi_aritmatika(a, b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    return tambah, kurang, kali, bagi

print("\nFungsi dengan multiple return values:")
a, b, c, d = operasi_aritmatika(10, 2)
print(f"10 + 2 = {a}")
print(f"10 - 2 = {b}")
print(f"10 * 2 = {c}")
print(f"10 / 2 = {d}")

# Lambda function (anonymous function)
print("\nLambda function:")
kuadrat = lambda x: x**2
print(f"Kuadrat dari 5 adalah {kuadrat(5)}")

# Menggunakan lambda dengan built-in functions
angka = [1, 5, 4, 3, 2, 6]
angka_urut = sorted(angka)
print(f"Sorted: {angka_urut}")

# Menggunakan fungsi sebagai argumen
def apply_operation(a, b, operation):
    return operation(a, b)

print("\nFungsi sebagai argumen:")
add = lambda x, y: x + y
multiply = lambda x, y: x * y

print(f"5 + 3 = {apply_operation(5, 3, add)}")
print(f"5 * 3 = {apply_operation(5, 3, multiply)}")

# List - koleksi data yang terurut dan bisa diubah
print("LIST OPERATIONS")
print("--------------")

# Membuat list
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]
print("List buah:", buah)

# Mengakses elemen list
print("\nMengakses elemen list:")
print("Buah pertama:", buah[0])
print("Buah terakhir:", buah[-1])  # Indeks negatif menghitung dari belakang

# Slicing list
print("\nSlicing list:")
print("Dua buah pertama:", buah[0:2])  # Indeks 0 dan 1
print("Dua buah terakhir:", buah[-2:])  # Dua terakhir

# Mengubah elemen list
print("\nMengubah elemen list:")
buah[1] = "Strawberry"
print("Setelah mengubah buah[1]:", buah)

# Metode list
print("\nMetode list:")

# Menambah elemen
buah.append("Anggur")
print("Setelah append Anggur:", buah)

buah.insert(2, "Durian")
print("Setelah insert Durian di indeks 2:", buah)

# Menghapus elemen
removed = buah.pop()
print(f"Elemen yang dihapus dengan pop(): {removed}")
print("List setelah pop():", buah)

buah.remove("Durian")
print("List setelah remove('Durian'):", buah)

# List operations
print("\nList operations:")
print("Jumlah elemen:", len(buah))
print("Apel di indeks:", buah.index("Apel"))

# Sorting list
angka = [3, 1, 4, 1, 5, 9, 2]
print("\nList angka:", angka)

angka.sort()
print("Setelah sort():", angka)

angka.reverse()
print("Setelah reverse():", angka)

# Nested list
print("\nNested list:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("matrix[1][2]:", matrix[1][2])  # Mengakses elemen baris 1, kolom 2 (nilai 6)

# Dictionary - koleksi key-value yang tidak berurutan
print("\n\nDICTIONARY OPERATIONS")
print("--------------------")

# Membuat dictionary
mahasiswa = {
    "nama": "Budi Santoso",
    "nim": "20210001",
    "jurusan": "Teknik Informatika",
    "usia": 20
}
print("Dictionary mahasiswa:", mahasiswa)

# Mengakses nilai dengan key
print("\nMengakses nilai dengan key:")
print("Nama:", mahasiswa["nama"])
print("NIM:", mahasiswa["nim"])

# Mengakses dengan get() (lebih aman)
print("\nMengakses dengan get():")
print("Jurusan:", mahasiswa.get("jurusan"))
print("IPK:", mahasiswa.get("ipk", "Data tidak tersedia"))  # Default jika key tidak ada

# Mengubah nilai
print("\nMengubah nilai:")
mahasiswa["usia"] = 21
print("Setelah mengubah usia:", mahasiswa)

# Menambah pasangan key-value baru
mahasiswa["ipk"] = 3.75
print("Setelah menambah IPK:", mahasiswa)

# Menghapus item
print("\nMenghapus item:")
del mahasiswa["usia"]
print("Setelah menghapus usia:", mahasiswa)

# Dictionary methods
print("\nDictionary methods:")
print("Keys:", list(mahasiswa.keys()))
print("Values:", list(mahasiswa.values()))
print("Items:", list(mahasiswa.items()))

# Looping dictionary
print("\nLooping dictionary:")
for key in mahasiswa:
    print(f"{key}: {mahasiswa[key]}")

print("\nLooping items:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Nested dictionary
print("\nNested dictionary:")
kampus = {
    "fakultas": {
        "FTIK": ["Informatika", "Sistem Informasi"],
        "FTI": ["Teknik Elektro", "Teknik Mesin"]
    },
    "alamat": "Jl. Pendidikan No. 1"
}
print("Kampus:", kampus)
print("Prodi di FTIK:", kampus["fakultas"]["FTIK"])