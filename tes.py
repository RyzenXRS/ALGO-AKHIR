import pandas as pd
import login as log

def dashboard(user):
    if user[2] == 'pembeli':
        print(
    f"""
    ╔═══════════════════════════════╗
    ║       Selamat Datang          ║
    ║┌─────────────────────────────┐║
    ║│  1. Tulis Resep             │║
    ║│  2. Rekomendasi Resep       │║
    ║│  3. Rekomend Bibit          │║
    ║│  4. Rekomendasi Pupuk       │║
    ║│  5. Keluar                  │║
    ║├─────────────────────────────┤║
    ║│  Pembeli : {user[0]}        │║
    ║└─────────────────────────────┘║
    ╚═══════════════════════════════╝
    """)
    elif user[2] == 'penjual':
        print(
    f"""
    ╔═══════════════════════════╗
    ║       Selamat Datang      ║
    ║┌─────────────────────────┐║
    ║│  1. Tambah Stok         │║
    ║│  2. Riwayat Tranksaksi  │║
    ║│  3. Rekap Penjualan     │║
    ║│  4. Keluar              │║
    ║├─────────────────────────┤║
    ║│  Penjual : {user[0]}    │║
    ║└─────────────────────────┘║
    ╚═══════════════════════════╝
    """)
    elif user[2] == 'admin':   
        print(
    f"""
    ╔═══════════════════════════╗
    ║       Selamat Datang      ║
    ║┌─────────────────────────┐║
    ║│  1. Tambah Saldo pengguna│║
    ║│  2. Buat voucher diskon │║
    ║│  3. Rekap Penjualan     │║
    ║│  4. Keluar              │║
    ║├─────────────────────────┤║
    ║│  Admin :  {user[0]}     │║
    ║└─────────────────────────┘║
    ╚═══════════════════════════╝
    """)

def tulis_resep():
    log.clear_terminal()
    file_resep = log.cek_file("list_resep.csv")

    nama_resep = input("Masukkan nama resep: ").capitalize()

    if not file_resep.empty:
        if nama_resep in file_resep['nama_resep'].values:
            print("Resep dengan nama tersebut sudah ada.")
            input("Tekan enter untuk kembali")
            return

    # deskripsi = input("Masukkan deskripsi resep: ")
    bahan = input("Masukkan bahan-bahan resep: ")

    
    tambah_resep = pd.DataFrame({
        'nama_resep': [nama_resep],
        'bahan': [bahan]
    })
    
    file_resep = pd.concat([file_resep, tambah_resep], ignore_index=True)
    file_resep.to_csv("list_resep.csv", index=False)

    print("Resep berhasil ditambahkan.")
    input("Tekan enter untuk kembali")
    return



    
def list_resep():
    log.clear_terminal()
    resep = log.cek_file("list_resep.csv")
    resep.index += 1
    print(resep[['nama_resep']])

    while True:
            
        try:
            input_resep = int(input("Resep mana yang kamu mau ? "))

            if 1 <= input_resep <= len(resep):
                match_resep = resep.iloc[[input_resep - 1]]  # Ambil resep berdasarkan nomor    
            # Tampilkan detail resep
                log.clear_terminal()
                print("\n==== Detail Resep ====")
                for col in match_resep.columns:
                    print(f"{col.capitalize()}: {match_resep[col].values[0]}")
                print()
            else:
                print("Nomor resep tidak valid. Coba lagi.")
                input("Tekan enter untuk coba lagi")
                continue

            
            
            lanjut = input("Apakah kamu lanjut mencari ? [y/t]").lower()

            if lanjut == 'y':
                log.clear_terminal()
                print(resep[['nama_resep']])
            elif lanjut == 't':
                log.clear_terminal()
                return
            else:
                print("Tidak ada pilihan !")

        except ValueError:
                print("Input harus berupa angka. Coba lagi.")

    

def pilih_dashboard(user):
    while True:
        pilihan = input("Pilih Menu [1/2/3/...]: ")
        if user[2] == "pembeli":
            match pilihan:
                case '1':
                    tulis_resep()
                    continue
                case '2':
                    list_resep()
                    continue
                case _:
                    print("Pilihan Tidak Ada\n")
                    input("Tekan Enter untuk mencoba kembali.")
                    continue
        elif user[2] == "penjual":
            match pilihan:           
                case _:
                    print("Pilihan Tidak Ada\n")
                    input("Tekan Enter untuk mencoba kembali.")
                    continue
        
        elif user[2] == "admin":
            match pilihan:
                case _:
                    print("Pilihan Tidak Ada\n")
                    input("Tekan Enter untuk mencoba kembali.")
                    continue
        break