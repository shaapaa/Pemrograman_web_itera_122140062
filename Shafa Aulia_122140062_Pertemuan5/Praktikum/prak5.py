# Membuat class Mahasiswa
class Mahasiswa:
    # Atribut Class (shared by all instances)
    jurusan = "Teknik Informatika"
    
    # Constructor/initializer
    def __init__(self, nama, nim):
        # Atribut Instance (unique for each instance)
        self.nama = nama
        self.nim = nim
        
    # Method
    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        
    def update_nama(self, nama_baru):
        self.nama = nama_baru
        print(f"Nama berhasil diubah menjadi {nama_baru}")

# Membuat object (instance) dari class Mahasiswa
mhs1 = Mahasiswa("Budi Santoso", "TI12345")
mhs2 = Mahasiswa("Ani Wijaya", "TI67890")

# Mengakses atribut
print(f"Mahasiswa 1: {mhs1.nama}, NIM: {mhs1.nim}")
print(f"Mahasiswa 2: {mhs2.nama}, NIM: {mhs2.nim}")

# Memanggil method
print("\nInformasi Mahasiswa 1:")
mhs1.display_info()

print("\nInformasi Mahasiswa 2:")
mhs2.display_info()

# Mengubah atribut
mhs1.update_nama("Budi Prakoso")

# Mengubah class attribute (berlaku untuk semua instance)
Mahasiswa.jurusan = "Informatika"
print("\nSetelah perubahan jurusan:")
mhs1.display_info()
mhs2.display_info()

# Class dasar
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
        self.odometer = 0
        
    def deskripsi(self):
        return f"{self.merek} ({self.tahun})"
    
    def baca_odometer(self):
        return f"Kendaraan ini telah berjalan sejauh {self.odometer} kilometer"
    
    def update_odometer(self, km):
        if km >= self.odometer:
            self.odometer = km
        else:
            print("Anda tidak dapat mengubah odometer!")

# Class turunan (inherited)
class Mobil(Kendaraan):
    def __init__(self, merek, tahun, tipe):
        # Memanggil constructor class parent
        super().__init__(merek, tahun)
        # Attribute tambahan
        self.tipe = tipe
        self.bensin = 100  # capacity in liters
        
    # Method tambahan
    def isi_bensin(self, liter):
        self.bensin += liter
        return f"Bensin diisi sebanyak {liter} liter. Total: {self.bensin} liter"
    
    # Method overriding
    def deskripsi(self):
        # Extend method dari parent class
        base_desc = super().deskripsi()
        return f"{base_desc} - {self.tipe}"

# Class turunan kedua
class Motor(Kendaraan):
    def __init__(self, merek, tahun, cc):
        super().__init__(merek, tahun)
        self.cc = cc
    
    def deskripsi(self):
        return f"{self.merek} ({self.tahun}) - {self.cc}cc"

# Membuat instance
kendaraan1 = Kendaraan("Generic", 2020)
mobil1 = Mobil("Toyota", 2022, "SUV")
motor1 = Motor("Honda", 2021, 150)

# Menggunakan method dari class dasar
print(kendaraan1.deskripsi())
print(mobil1.deskripsi())  # Method yang di-override
print(motor1.deskripsi())  # Method yang di-override

# Menggunakan method dari class dasar yang diwarisi
mobil1.update_odometer(1500)
print(mobil1.baca_odometer())

# Menggunakan method dari class turunan
print(mobil1.isi_bensin(20))

