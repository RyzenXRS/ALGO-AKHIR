import pandas as pd
import random
import os 
import login as log

status_login = False

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear' )

def cek_file(file):
    try:
        return pd.read_csv(f"{file}")
    except FileNotFoundError:
        print("File tidak di temukan. \n Periksa kembali lokasi file")

def login():
    global status_login
    data = cek_file('data_login.csv')

    username = input("Masukkan Username : ").strip()
    password = input("Masukkan Password : ").strip()

    user = data[
        (data['username'] == username) &
        (data['password'] == password) 
    ] 
    usn = user.iloc[0]['username']
    psw = user.iloc[0]['password']
    role = user.iloc[0]['role']

    status_login = True

    if len(user)>0:
        clear_terminal()
        print('=' * (36+len(role)))
        print(f"Selamat datang {username}, Kamu login sebagai {role}")
        print("Login Berhasil")
        print('=' * (36+len(role)))
        user_login = (usn,psw,role)
        return user_login
    else : 
        print("Salah Username / Password le")

def buat_akun():
    data = cek_file("data_login.csv")
        
    nama = input("Masukkan nama : ").strip()

    #Cek nama pada database
    if nama in data['username'].values:
        print("Username tidak tersedia. Silahkan coba lagi !")
        print("Tekan enter untuk coba kembali")
    else:
        print(f"Berhasil menambahkan {nama} ke dalam database !")
    
    password = input("Masukkan password : ").strip()
    print("-" * 26)
    print("Daftar Sebagai : ")
    print(" [1] Pembeli")
    print(" [2] Penjual")
    print(" [3] Batal")
    print("-" * 26)
    while True: 
        pilih = input("Pilih menu [1/2/3]:")
        match pilih:
            case '1':
                tambah_user = pd.DataFrame({
                    'username' : [nama],
                    'password' : [password],
                    'role' : ['pembeli']
                })
                users = pd.concat([data, tambah_user])
                users.to_csv("data_login.csv", index=False)

                print("\n==== Registrasi berhasil! ====")
                print(f"'{nama}' telah ditambahkan sebagai Pembeli baru.")
                print("Selamat Datang di Aplikasi TetaBiz masukkan kode : XUSAS untuk mendapatkan diskon !!")
                input("Tekan Enter untuk kembali ke Menu.")
                break
            case '2':
                tambah_user = pd.DataFrame({
                    'username' : [nama],
                    'password' : [password],
                    'role' : ['penjual']
                })
                users = pd.concat([data, tambah_user])
                users.to_csv("data_login.csv", index=False)

                print("\n==== Registrasi berhasil! ====")
                print(f"'{nama}' telah ditambahkan sebagai Penjual baru.")
                print("Selamat Datang di Aplikasi TetaBiz masukkan kode : XUSAS untuk mendapatkan diskon !!")
                input("Tekan Enter untuk kembali ke Menu.")
            case '3':
                print("=" * 40)
                print("Pembuatan Akun di Batalkan")
                input("Tekan Enter untuk kembali ke Menu.")
                return
            case _:
                print("Pilihan tidak ada")
                input("Tekan enter untuk mencoba kembali")
                            
def logout():
    global status_login  # Mengakses variabel global login_status
    if status_login:
        clear_terminal()
        print("=" * 19)
        print("= Logout Berhasil =")
        print("=" * 19)
        input("Tekan Enter untuk melanjutkan.")

        status_login = False  # Mengubah status login menjadi False setelah logout
        return status_login
    else:
        print("Anda belum login.")
        input("Tekan Enter untuk melanjutkan.")

            
def menu_tampilan():
    clear_terminal()
    print(
"""
╔══════════════════╗
║  Selamat Datang  ║
║┌────────────────┐║
║│  1. Login      │║
║│  2. Register   │║
║│  3. Keluar     │║    
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
                print("Terima kasih !")
                return pilihan
            case _:
                print("Pilihan yang kamu pilih tidak ada")