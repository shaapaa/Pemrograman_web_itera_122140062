# Soal 2 
# program pengelolaan data nilai mahasiswa

# List Data Mahasiswa (nama, nim, nilai_uts, nilai_uas, nilai_tugas)
mahasiswa = [
    {"nama": "Fajar", "nim": "12011110", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 90},
    {"nama": "Thoro", "nim": "12011111", "nilai_uts": 90, "nilai_uas": 90, "nilai_tugas": 95},
    {"nama": "Adit", "nim": "12011144", "nilai_uts": 60, "nilai_uas": 75, "nilai_tugas": 85},
    {"nama": "Denis", "nim": "12011198", "nilai_uts": 40, "nilai_uas": 50, "nilai_tugas": 60},
    {"nama": "Adel", "nim": "10111876", "nilai_uts": 70, "nilai_uas": 65, "nilai_tugas": 80},
]

# Hitung nilai akhir dan grade
for mhs in mahasiswa:
    nilai_akhir = 0.3 * mhs["nilai_uts"] + 0.4 * mhs["nilai_uas"] + 0.3 * mhs["nilai_tugas"]
    mhs["nilai_akhir"] = round(nilai_akhir, 2)
    if nilai_akhir >= 80:
        mhs["grade"] = "A"
    elif nilai_akhir >= 70:
        mhs["grade"] = "B"
    elif nilai_akhir >= 60:
        mhs["grade"] = "C"
    elif nilai_akhir >= 50:
        mhs["grade"] = "D"
    else:
        mhs["grade"] = "E"

# Menampilkan data
print(f"{'Nama':<10} {'NIM':<10} {'Akhir':<8} {'Grade':<6}")
print("-" * 40)
for mhs in mahasiswa:
    print(f"{mhs['nama']:<10} {mhs['nim']:<10} {mhs['nilai_akhir']:<8} {mhs['grade']:<6}")

# Mahasiswa nilai tertinggi dan terendah
tertinggi = max(mahasiswa, key=lambda x: x['nilai_akhir'])
terendah = min(mahasiswa, key=lambda x: x['nilai_akhir'])

print(f"\nMahasiswa nilai tertinggi: {tertinggi['nama']} - {tertinggi['nilai_akhir']}")
print(f"Mahasiswa nilai terendah: {terendah['nama']} - {terendah['nilai_akhir']}")
