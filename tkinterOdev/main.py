import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Odev")
pencere.resizable(width=False ,height=False)
connection = mysql.connector.connect(host='localhost', user='root',
                                     password='', port='3306', database='odev1')
c = connection.cursor()

def Kapat():
    pencere.destroy()

def Gonder():
    try:
        ad = adGir.get()
        soyad = soyadGir.get()
        yas = yasGir.get()
        insert_query = "INSERT INTO `kullanici`(`ad`, `soyad`, `yas`) VALUES (%s,%s,%s)"
        vals = (ad,soyad,yas)
        c.execute(insert_query,vals)
        connection.commit()
        mesaj = messagebox.showinfo(
            title="Bilgi",
            message="Gonderildi!"
        )
    except:
        hata = messagebox.showwarning(
            title="Uyarı",
            message="Veri Girmediniz!"
        )

def VeriGoster():
    c.execute('SELECT * FROM `kullanici`')
    kullaniciler = c.fetchall()
    for kullanici in kullaniciler:
        tablo.insert('','end', value=(kullanici[0], kullanici[1],kullanici[2], kullanici[3]))

def Guncelle():
    for item in tablo.get_children():
        tablo.delete(item)
    VeriGoster()

bilesenler = ttk.Notebook(
    pencere,
    width=550,
    height=400
)
bilesenler.place(x=25,y=25)

bilesen1 = ttk.Frame(
    bilesenler,
    width=50,
    height=50,
)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)

bilesenler.add(
    bilesen1,
    text="Veri Gonder"
)

bilesenler.add(
    bilesen2,
    text="Veri Goruntule"
)

gonderButonu = tk.Button(
    bilesen1,
    text="Gonder",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    width=5,
    cursor="hand2",
    command=Gonder
)

kapatButonu = tk.Button(
    bilesen1,
    text="Kapat",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    width=5,
    cursor="hand2",
    command=Kapat
)

etiket1 = tk.Label(
    bilesen1,
    text="Ad:",
    width=5
)

etiket2 = tk.Label(
    bilesen1,
    text="Soyad:",
    width=5
)

etiket3 = tk.Label(
    bilesen1,
    text="Yaş:",
    width=5
)

adGir = tk.Entry(
    bilesen1
)

soyadGir = tk.Entry(
    bilesen1
)

yasGir = tk.Entry(
    bilesen1,
    width=5
)


tablo = ttk.Treeview(
    bilesen2,
    columns=(1,2,3,4),
    height=15,
    show="headings"
)
tablo.column(1, anchor=CENTER, stretch=NO, width=125)
tablo.column(2, anchor=CENTER, stretch=NO, width=125)
tablo.column(3, anchor=CENTER, stretch=NO, width=125)
tablo.column(4, anchor=CENTER, stretch=NO, width=125)

tablo.heading(1, text="ID")
tablo.heading(2, text="Ad")
tablo.heading(3, text="Soyad")
tablo.heading(4, text="Yas")

guncelleme = tk.Button(
    bilesen2,
    text="Guncelle",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    width=5,
    cursor="hand2",
    command=Guncelle
)


etiket1.place(x=150,y=100)
etiket2.place(x=150,y=150)
etiket3.place(x=200,y=200)

adGir.place(x=200,y=100)
soyadGir.place(x=200,y=150)
yasGir.place(x=260,y=200)

gonderButonu.place(x=150,y=300)
kapatButonu.place(x=325,y=300)


tablo.pack()
guncelleme.pack(pady=25)
VeriGoster()

pencere.mainloop()