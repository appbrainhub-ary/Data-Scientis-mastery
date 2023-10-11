from tkinter import *

def hitung_skor():
    par = int(entry_par.get())
    pukulan = int(entry_pukulan.get())
    
    skor_hole = pukulan - par
    
    label_skor.config(text="Skor: " + str(skor_hole))

root = Tk()
root.title("Penghitung Skor Golf")
root.geometry("500x290")

# Mengatur latar belakang dengan gambar
background_image = PhotoImage(file="background.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


from tkinter.font import Font
bold_font = Font(family="Arial", size=12, weight="bold")
label = Label(root, text="Aplikasi Scorecard Golf Club", wraplength=270, font=bold_font)
label.pack(pady=10)


label_par = Label(root, text="Masukkan jumlah par:", bg="lightblue")
label_par.pack()

entry_par = Entry(root)
entry_par.pack()

label_pukulan = Label(root, text="Masukkan jumlah pukulan:", bg="lightblue")
label_pukulan.pack()

entry_pukulan = Entry(root)
entry_pukulan.pack()

button = Button(root, text="Hitung Skor", command=hitung_skor)
button.pack()

label_skor = Label(root, text="Skor: ", bg="yellow")
label_skor.pack()

root.mainloop()
