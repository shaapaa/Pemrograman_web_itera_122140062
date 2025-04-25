# Soal 1
# Program penghitung BMI

berat = float(input("Masukkan berat badan anda (kg): "))
tinggi = float(input("Masukkan tinggi badan anda (m): "))

#Rumus BMI
bmi = berat / (tinggi ** 2)

print(f"\nBMI Anda: {bmi:.2f}") # Menampilkan hasil BMI

#Percabangan untuk menentukan kategori BMI
if bmi < 18.5:
    kategori = "Berat badan anda kurang"
elif bmi < 25:
    kategori = "Berat badan anda normal"
elif bmi < 30:
    kategori = "Berat badan anda berlebih"
else:
    kategori = "Obesitas"

print(f"Kategori BMI: {kategori}")
