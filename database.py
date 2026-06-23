import csv
import os

FILE_CSV = os.path.join(os.path.dirname(__file__), "kursus.csv")


def baca_data():
    data = []

    try:
        with open(FILE_CSV, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

    except FileNotFoundError:
        pass

    return data


def simpan_data(data):
    fieldnames = [
        "id_kursus",
        "nama_kursus",
        "pengajar",
        "durasi",
        "kuota"
    ]

    with open(FILE_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


def tambah_kursus():

    data = baca_data()

    id_kursus = input("ID Kursus : ")

    for kursus in data:
        if kursus["id_kursus"] == id_kursus:
            print("ID Kursus sudah digunakan!")
            return

    kursus_baru = {
        "id_kursus": id_kursus,
        "nama_kursus": input("Nama Kursus : "),
        "pengajar": input("Pengajar : "),
        "durasi": input("Durasi (Jam) : "),
        "kuota": input("Kuota Peserta : ")
    }

    data.append(kursus_baru)

    simpan_data(data)

    print("Kursus berhasil ditambahkan.")


def tampilkan_kursus():

    data = baca_data()

    if not data:
        print("Belum ada data kursus.")
        return

    print("\n===== DATA KURSUS =====")

    for kursus in data:

        print("-" * 40)
        print("ID Kursus   :", kursus["id_kursus"])
        print("Nama Kursus :", kursus["nama_kursus"])
        print("Pengajar    :", kursus["pengajar"])
        print("Durasi      :", kursus["durasi"])
        print("Kuota       :", kursus["kuota"])


def update_kursus():

    data = baca_data()

    id_kursus = input("Masukkan ID Kursus : ")

    ditemukan = False

    for kursus in data:

        if kursus["id_kursus"] == id_kursus:

            ditemukan = True

            kursus["nama_kursus"] = input("Nama Kursus Baru : ")
            kursus["pengajar"] = input("Pengajar Baru : ")
            kursus["durasi"] = input("Durasi Baru : ")
            kursus["kuota"] = input("Kuota Baru : ")

            break

    if ditemukan:

        simpan_data(data)

        print("Data berhasil diupdate.")

    else:

        print("ID Kursus tidak ditemukan.")


def hapus_kursus():

    data = baca_data()

    id_kursus = input("Masukkan ID Kursus : ")

    data_baru = []

    ditemukan = False

    for kursus in data:

        if kursus["id_kursus"] == id_kursus:

            ditemukan = True

        else:

            data_baru.append(kursus)

    if ditemukan:

        simpan_data(data_baru)

        print("Data berhasil dihapus.")

    else:

        print("ID Kursus tidak ditemukan.")


def cari_kursus():

    data = baca_data()

    id_kursus = input("Masukkan ID Kursus : ")

    for kursus in data:

        if kursus["id_kursus"] == id_kursus:

            print("\n===== DATA DITEMUKAN =====")
            print("ID Kursus   :", kursus["id_kursus"])
            print("Nama Kursus :", kursus["nama_kursus"])
            print("Pengajar    :", kursus["pengajar"])
            print("Durasi      :", kursus["durasi"])
            print("Kuota       :", kursus["kuota"])

            return

    print("Data tidak ditemukan.")


def urutkan_kursus():

    data = baca_data()

    data.sort(key=lambda x: x["nama_kursus"])

    print("\n===== DATA KURSUS TERURUT =====")

    for kursus in data:

        print("-" * 40)
        print("ID Kursus   :", kursus["id_kursus"])
        print("Nama Kursus :", kursus["nama_kursus"])
        print("Pengajar    :", kursus["pengajar"])
        print("Durasi      :", kursus["durasi"])
        print("Kuota       :", kursus["kuota"])