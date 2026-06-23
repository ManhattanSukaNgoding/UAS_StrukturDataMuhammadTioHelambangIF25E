from collections import deque
from database import *

antrian = deque()

while True:

    print("\n")
    print("===== SISTEM MANAJEMEN KURSUS =====")
    print("1. Tambah Kursus")
    print("2. Tampilkan Kursus")
    print("3. Update Kursus")
    print("4. Hapus Kursus")
    print("5. Cari Kursus")
    print("6. Urutkan Kursus")
    print("7. Daftar Peserta")
    print("8. Layani Peserta")
    print("9. Lihat Antrian")
    print("0. Keluar")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        tambah_kursus()

    elif pilihan == "2":
        tampilkan_kursus()

    elif pilihan == "3":
        update_kursus()

    elif pilihan == "4":
        hapus_kursus()

    elif pilihan == "5":
        cari_kursus()

    elif pilihan == "6":
        urutkan_kursus()

    elif pilihan == "7":

        nama = input("Nama Peserta : ")

        antrian.append(nama)

        print(f"{nama} berhasil masuk antrian.")

    elif pilihan == "8":

        if len(antrian) > 0:
            peserta = antrian.popleft()
            print(f"Sedang melayani {peserta}")

        else:
            print("Antrian kosong.")

    elif pilihan == "9":

        if len(antrian) == 0:
            print("Antrian kosong.")

        else:
            print("\n===== DAFTAR ANTRIAN =====")

            nomor = 1

            for nama in antrian:
                print(f"{nomor}. {nama}")
                nomor += 1

    elif pilihan == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")