# Kelas berdasarkan akhiran NRP
def tentukan_kelas(nrp_akhir):
    # Mengonversi input menjadi integer
    nrp_akhir = int(nrp_akhir)

    # Menentukan kelas berdasarkan rentang NRP
    if 1 <= nrp_akhir <= 100:
        if nrp_akhir % 2 == 0:
            return "K2"
        else:
            return "K1"
    elif 101 <= nrp_akhir <= 200:
        if nrp_akhir % 2 == 0:
            return "K4"
        else:
            return "K3"
    elif 201 <= nrp_akhir <= 300:
        if nrp_akhir % 2 == 0:
            return "K6"
        else:
            return "K5"
    elif nrp_akhir > 300:
        if nrp_akhir % 2 == 0:
            return "K8"
        else:
            return "K7"
    else:
        return "NRP tidak valid"

# Input akhiran NRP dari pengguna
nrp_akhir = input("Masukan akhiran NRP: ")
kelas = tentukan_kelas(nrp_akhir)

# Menampilkan hasil
print(f"Mahasiswa masuk ke kelas {kelas}")