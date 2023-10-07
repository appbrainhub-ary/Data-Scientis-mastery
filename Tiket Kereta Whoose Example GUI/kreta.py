import tkinter as tk
from tkinter import messagebox

def pesan_tiket():
    nama_pemesan = entry_nama.get()
    nomor_antrian = entry_antrian.get()
    tujuan = "Jakarta - Bandung"

    # Proses pemesanan tiket
    # ...

    # Menampilkan notifikasi message box
    messagebox.showinfo("Pemesanan Tiket", "Tiket berhasil dipesan!\nNama Pemesan: {}\nNomor Antrian: {}\nTujuan: {}".format(nama_pemesan, nomor_antrian, tujuan))

# Membuat window
window = tk.Tk()
window.title("Aplikasi Pemesanan Tiket Kereta")
window.geometry("500x290")

# Menambahkan gambar background
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

from tkinter.font import Font
bold_font = Font(family="Helvetica", size=11, weight="bold")
label = tk.Label(window, text="Aplikasi Pemesanan Tiket Kereta Cepat Whoosh.", wraplength=270, font=bold_font)
label.pack(pady=10)

# Membuat label dan entry untuk nama pemesan
label_nama = tk.Label(window, text="Nama Pemesan:")
label_nama.pack()
entry_nama = tk.Entry(window)
entry_nama.pack()

# Membuat label dan entry untuk nomor antrian
label_antrian = tk.Label(window, text="Nomor Antrian:")
label_antrian.pack()
entry_antrian = tk.Entry(window)
entry_antrian.pack()

# Membuat tombol untuk pesan tiket
button_pesan = tk.Button(window, text="Pesan Tiket", command=pesan_tiket)
button_pesan.pack()

# Menjalankan aplikasi
window.mainloop()
