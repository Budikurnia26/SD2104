# H01_NRP_01.py

# Fungsi untuk menghitung keuntungan
def hitung_keuntungan(harga_dasar, harga_jual):
    return harga_jual - harga_dasar

# Input harga dasar dan harga jual untuk masing-masing barang
harga_dasar_A = float(input("Masukkan harga dasar barang A: "))
harga_jual_A = float(input("Masukkan harga jual barang A: "))

harga_dasar_B = float(input("Masukkan harga dasar barang B: "))
harga_jual_B = float(input("Masukkan harga jual barang B: "))

harga_dasar_C = float(input("Masukkan harga dasar barang C: "))
harga_jual_C = float(input("Masukkan harga jual barang C: "))

# Menghitung keuntungan untuk setiap barang
keuntungan_A = hitung_keuntungan(harga_dasar_A, harga_jual_A)
keuntungan_B = hitung_keuntungan(harga_dasar_B, harga_jual_B)
keuntungan_C = hitung_keuntungan(harga_dasar_C, harga_jual_C)

# Menentukan barang dengan keuntungan terbesar
if keuntungan_A > keuntungan_B and keuntungan_A > keuntungan_C:
    barang_terbaik = "A"
elif keuntungan_B > keuntungan_A and keuntungan_B > keuntungan_C:
    barang_terbaik = "B"
else:
    barang_terbaik = "C"

# Menampilkan hasil
print(f"Barang yang harus ditawarkan adalah barang {barang_terbaik}")