import pandas as pd
import random
import os 

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear' )

def login():
    data = pd.read_csv('data_login.csv')

    username = input("Masukkan Username : ").strip()
    password = input("Masukkan Password : ").strip()

    user = data[
        (data['username'] == username) &
        (data['password'] == password) 
    ] 
    usn = data.iloc[0]['username']
    psw = data.iloc[0]['password']
    role = data.iloc[0]['role']

    if len(user)>0:
        clear_terminal()
        print(f"Selamat datang {username}, Kamu login sebagai {role}")
        print("Login Berhasil")
        user_login = (usn,psw,role)
        program()
        return user_login
    else : 
        print("Salah Username / Password le")

def buat_akun():
    data = pd.read_csv("data_login.csv")
        
    nama = input("Masukkan nama : ").strip()
    if nama in data['username'].values:
        print("Username tidak tersedia. Silahkan coba lagi !")
        print("Tekan enter untuk coba kembali")
    else:
        print(f"Berhasil menambahkan {nama} ke dalam database !")
    
    password = input("Masukkan password : ").strip()
    tambah_user = pd.DataFrame({
        'username' : [nama],
        'password' : [password]
    })
    users = pd.concat([data, tambah_user])
    users.to_csv("data_login.csv", index=False)

    print("\n==== Registrasi berhasil! ====")
    print(f"'{nama}' telah ditambahkan sebagai anggota baru.")
    print("Selamat Datang di Aplikasi TetaBiz masukkan kode : XUSAS untuk mendapatkan diskon !!")
    input("Tekan Enter untuk kembali ke Menu.")
    menu()

def list_resep():
    resep = pd.read_csv("list_resep.csv")

    nama_resep = resep[['nama_resep']]


def program():
    while True:
        angka = int(input("Masukkan angka kamu : "))
        angka_random = random.randint(0,100)

        if angka > 100: 
            print("Angka tidak boleh lebih dari 100")
        else:
            if angka == angka_random:
                print("Kamu benar menebak angka !!")
            else: 
                print("Kamu kurang beruntung")
                print(f"Jawaban : {angka_random} ")

        inputan_stop = input("Apakah kamu ingin lanjut [y/t] : ").lower()
        if inputan_stop == 't':
            break
        elif inputan_stop == 'y':
            clear_terminal()
            program()
        else:
            print("Tidak ada pilihan !")
            

            
def menu_tampilan():
    clear_terminal()
    print(
"""
╔══════════════════╗
║  Selamat Datang  ║
║┌────────────────┐║
║│  1. Login      │║
║│  2. Register   │║
║│  3. Ide resep  │║
║│  4. Keluar     │║
║├────────────────┤║
║│   Login Page   │║
║└────────────────┘║
╚══════════════════╝
""")
  

def menu():
    menu_tampilan()
    while True:
        pilihan = input("Masukkan pilihan [1,2,3] : ")

        match pilihan:
            case "1":
                login()
                return pilihan
            case "2":
                buat_akun()
                return pilihan
            case "3":
                print("Mainenance bentar yach")
                # list_resep():
                return pilihan
            case "4":
                print("Terima kasih !")
                return pilihan
            case _:
                print("Pilihan yang kamu pilih tidak ada")
            

menu()