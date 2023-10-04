import tkinter as tk
import json



def lihat_data():
    # Membaca data proyek dari file
    with open("data_proyek.json", "r") as file:
        data_proyek = json.load(file)

    # Menampilkan data proyek
    for proyek in data_proyek:
        nama = proyek["nama"]
        deskripsi = proyek["deskripsi"]
        label = tk.Label(window, text=f"Nama Proyek: {nama}\nDeskripsi Proyek: {deskripsi}")
        label.pack()

def tambah_data():
    # Membaca data proyek yang sudah ada dari file
    try:
        with open("data_proyek.json", "r") as file:
            data_proyek = json.load(file)
    except FileNotFoundError:
        data_proyek = []

    # Membuat jendela pop-up untuk memasukkan data proyek baru
    popup = tk.Toplevel(window)
    popup.title("Tambah Data Proyek")

    nama_label = tk.Label(popup, text="Nama Proyek:")
    nama_label.pack()
    nama_entry = tk.Entry(popup)
    nama_entry.pack()

    deskripsi_label = tk.Label(popup, text="Deskripsi Proyek:")
    deskripsi_label.pack()
    deskripsi_entry = tk.Entry(popup)
    deskripsi_entry.pack()

    def simpan_data():
        # Mengambil data yang dimasukkan
        nama_proyek = nama_entry.get()
        deskripsi_proyek = deskripsi_entry.get()

        # Menambahkan data proyek baru ke dalam list
        data_proyek.append({
            "nama": nama_proyek,
            "deskripsi": deskripsi_proyek
        })

        # Menyimpan data proyek ke dalam file
        with open("data_proyek.json", "w") as file:
            json.dump(data_proyek, file)

        # Menutup jendela pop-up
        popup.destroy()

        # Menampilkan pesan sukses
        tk.messagebox.showinfo("Sukses", "Proyek berhasil ditambahkan!")

    simpan_button = tk.Button(popup, text="Simpan", command=simpan_data)
    simpan_button.pack()

def edit_data():
    # Membaca data proyek dari file
    with open("data_proyek.json", "r") as file:
        data_proyek = json.load(file)

    # Membuat jendela pop-up untuk memilih proyek yang akan diedit
    popup = tk.Toplevel(window)
    popup.title("Edit Data Proyek")

    # Menampilkan data proyek yang ada
    for i, proyek in enumerate(data_proyek):
        nama = proyek["nama"]
        label = tk.Label(popup, text=f"{i+1}. {nama}")
        label.pack()

    # Memilih proyek yang akan diedit
    pilihan_label = tk.Label(popup, text="Pilih nomor proyek yang ingin diedit:")
    pilihan_label.pack()
    pilihan_entry = tk.Entry(popup)
    pilihan_entry.pack()

    def edit_proyek():
        # Mengambil pilihan proyek yang dipilih
        index_proyek = int(pilihan_entry.get()) - 1

        # Membuat jendela pop-up untuk mengedit data proyek
        edit_popup = tk.Toplevel(window)
        edit_popup.title("Edit Data Proyek")

        nama_label = tk.Label(edit_popup, text="Nama Proyek Baru:")
        nama_label.pack()
        nama_entry = tk.Entry(edit_popup)
        nama_entry.pack()

        deskripsi_label = tk.Label(edit_popup, text="Deskripsi Proyek Baru:")
        deskripsi_label.pack()
        deskripsi_entry = tk.Entry(edit_popup)
        deskripsi_entry.pack()

        def simpan_perubahan():
            # Mengambil data proyek yang baru
            nama_proyek_baru = nama_entry.get()
            deskripsi_proyek_baru = deskripsi_entry.get()

            # Mengubah data proyek yang dipilih dengan data yang baru
            data_proyek[index_proyek]["nama"] = nama_proyek_baru
            data_proyek[index_proyek]["deskripsi"] = deskripsi_proyek_baru

            # Menyimpan data proyek ke dalam file
            with open("data_proyek.json", "w") as file:
                json.dump(data_proyek, file)

            # Menutup jendela pop-up
            edit_popup.destroy()

            # Menampilkan pesan sukses
            tk.messagebox.showinfo("Sukses", "Proyek berhasil diedit!")

        simpan_button = tk.Button(edit_popup, text="Simpan", command=simpan_perubahan)
        simpan_button.pack()

    edit_button = tk.Button(popup, text="Edit", command=edit_proyek)
    edit_button.pack()

# Membuat jendela utama
window = tk.Tk()
window.title("Aplikasi Perencanaan dan Pengelolaan Proyek")

from tkinter.font import Font
bold_font = Font(family="Helvetica", size=11, weight="bold")
label = tk.Label(window, text="Aplikasi Perencanaan dan Pengelolaan Proyek PNS", font=bold_font)

label.pack()

window.geometry("400x300")

# Membuat tombol untuk melihat data proyek
lihat_button = tk.Button(window, text="Lihat Data Proyek", command=lihat_data)
lihat_button.pack()

# Membuat tombol untuk tambah data proyek
tambah_button = tk.Button(window, text="Tambah Data Proyek", command=tambah_data)
tambah_button.pack()

# Membuat tombol untuk edit data proyek
edit_button = tk.Button(window, text="Edit Data Proyek", command=edit_data)
edit_button.pack()

# Menjalankan aplikasi
window.mainloop()
