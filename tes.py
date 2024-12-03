import pandas as pd
import login as log
from tabulate import tabulate as tb

#================================================================================================
# MENU UTAMA DAN NAVIGASI
#================================================================================================
def dashboard(user):
    if user[2] == 'pembeli':
    #     menu = [
    # ["1. Aspirasi Resep"],
    # ["2. Rekomendasi Resep"],
    # ["3. Rekomend Bibit"],
    # ["4. Logout"],
    # [ f"Pembeli : {user[0]}"]
    # ]  
    #     print(tabulate(menu, headers=["Selamat Datang"], tablefmt="double_grid"))
        print(
    f"""
    ╔═══════════════════════════════╗
    ║       Selamat Datang          ║
    ║┌─────────────────────────────┐║
    ║│  1. Aspirasi Resep          │║
    ║│  2. Rekomendasi Resep       │║
    ║│  3. Rekomendasi Bibit       │║
    ║│  4. List Produk             │║
    ║│  5. Cari Produk             │║
    ║│  6. Logout                  │║
    ║├─────────────────────────────┤║
    ║│  Pembeli : {user[0]}{' '*(17-len(user[0]))}│║
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
    ║│  Penjual : {user[0]}{' '*(13-len(user[0]))}│║
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
    ║│  Admin :  {user[0]}{' '*(17-len(user[0]))}│║
    ║└─────────────────────────┘║
    ╚═══════════════════════════╝
    """)

def pilih_dashboard(user):
    while True:
        log.clear_terminal()
        dashboard(user)
        pilihan = input("Pilih Menu [1/2/3/...]: ")
        if user[2] == "pembeli":
            match pilihan:
                case '1':
                    tulis_resep()
                    continue
                case '2':
                    list_resep()
                    continue
                case '3':
                    rekom_bibit()
                    continue
                case '4':
                    list_produk()
                case '5':
                    print("Maintenance yachh")
                    # cari_produk()
                case '6':
                    print("Terima Kasih")
                    log.logout()
                    return
                case _:
                    print("Pilihan Tidak Ada\n")
                    input("Tekan Enter untuk mencoba kembali.")
                    continue
        elif user[2] == "penjual":
            match pilihan:
                case '1':
                    tambah_produk()
                    continue         
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

#================================================================================================
# FUNGSI FITUR FITUR
#================================================================================================
def tulis_resep():
    while True:
        log.clear_terminal()
        file_resep = log.cek_file("list_resep.csv")

        nama_resep = input("Masukkan nama resep: ").capitalize()

        if not file_resep.empty:
            if nama_resep in file_resep['nama_resep'].values:
                print("Resep dengan nama tersebut sudah ada.")
                input("Tekan enter untuk kembali")
                continue

        # deskripsi = input("Masukkan deskripsi resep: ")
        bahan = input("Masukkan bahan-bahan resep: ")

        
        tambah_resep = pd.DataFrame({
            'nama_resep': [nama_resep],
            'bahan': [bahan]
        })
        
        file_resep = pd.concat([file_resep, tambah_resep], ignore_index=True)
        file_resep.to_csv("list_resep.csv", index=False)

        lanjut = input("Apakah kamu ingin menambahkan aspirasi resep lagi [y/t] : ").lower()
        if lanjut == 'y':
            print(f"Resep {nama_resep}  berhasil ditambahkan.")
            continue
        else:
            print(f"Resep {nama_resep} berhasil ditambahkan.")
            input("Tekan enter untuk kembali")
            return

def rekom_bibit():
    while True:
        log.clear_terminal()
        tanaman = pd.read_csv("list_bibit.csv")

        tanaman.index += 1

        print("Daftar Tanaman:")
        nama_tanaman = tanaman[['Nama Tanaman']]
        print(tb(nama_tanaman, headers=["Nama Tanaman"], tablefmt="double_grid"))

        try:
            input_tanaman = int(input("Pilih nomor tanaman yang kamu mau: "))

            if input_tanaman in tanaman.index:
                print("\nKamu memilih tanaman:", tanaman.iloc[input_tanaman - 1]['Nama Tanaman'])
                
                # Menampilkan detail tanaman yang dipilih
                match_tanaman = tanaman.loc[input_tanaman]
                # print("\nDetail Tanaman yang Dipilih:")
                log.clear_terminal()
                detail = [
                ["Nama Tanaman", match_tanaman["Nama Tanaman"]],
                ["Jenis Tanaman", match_tanaman["Jenis Tanaman"]],
                ["Kebutuhan Air", match_tanaman["Kebutuhan Air"]],
                ["Kebutuhan Cahaya", match_tanaman["Kebutuhan Cahaya"]],
                ["Suhu Ideal", match_tanaman["Suhu Ideal"]]
                ]
            #     print("\n==== Detail Tanaman yang Dipilih ====")
            #     print(f"Nama Tanaman: {match_tanaman['Nama Tanaman']}")
            #     print(f"Jenis Tanaman: {match_tanaman['Jenis Tanaman']}")
            #     print(f"Kebutuhan Air: {match_tanaman['Kebutuhan Air']}")
            #     print(f"Kebutuhan Cahaya: {match_tanaman['Kebutuhan Cahaya']}")
            #     print(f"Suhu Ideal: {match_tanaman['Suhu Ideal']}")
            #     print("=======================================")
                print(tb(detail, headers=["Detail", "Tanaman yang Dipilih"], tablefmt="double_grid"))
            else:
                print("Nomor tanaman tidak ditemukan.")
                
            lanjutan = input("Apakah kamu ingin melihat rekomendasi resep lagi [y/t] : ").lower()
            if lanjutan == 'y':
                log.clear_terminal()
                continue
            else:
                input("Tekan enter untuk kembali")
                return
        except ValueError:
            print("Input tidak valid, harap masukkan nomor yang benar.")

def list_resep():
    while True:
        log.clear_terminal()
        resep = log.cek_file("list_resep.csv")
        resep.index += 1

        print("Daftar Resep : ")
        nama_resep = resep[['nama_resep']]

        print(tb(nama_resep, headers=["Nama Resep"], tablefmt="double_grid"))

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
                    continue

#================================================================================================
# FUNGSI FITUR FITUR
#================================================================================================

def tambah_stok():
    while True:
        log.clear_terminal()
        file_stock = log.cek_file("stok_produk.csv")

        nama_resep = input("Masukkan nama resep: ").capitalize()

        if not file_resep.empty:
            if nama_resep in file_resep['nama_resep'].values:
                print("Resep dengan nama tersebut sudah ada.")
                input("Tekan enter untuk kembali")
                continue

        # deskripsi = input("Masukkan deskripsi resep: ")
        bahan = input("Masukkan bahan-bahan resep: ")

        
        tambah_resep = pd.DataFrame({
            'nama_resep': [nama_resep],
            'bahan': [bahan]
        })
        
        file_resep = pd.concat([file_resep, tambah_resep], ignore_index=True)
        file_resep.to_csv("list_resep.csv", index=False)

        lanjut = input("Apakah kamu ingin menambahkan aspirasi resep lagi [y/t] : ").lower()
        if lanjut == 'y':
            print(f"Resep {nama_resep}  berhasil ditambahkan.")
            continue
        else:
            print(f"Resep {nama_resep} berhasil ditambahkan.")
            input("Tekan enter untuk kembali")
            return

def tambah_produk():
    pdProduk = log.cek_file("stok_produk.csv")
    pdview = pdProduk[pdProduk["view"]==1]  
    pdview = pdview.drop(columns=["view"],)

    # print(pdview.to_string(index=False))
    print(tb(pdview, headers=["ID", "Nama Produk", "Harga", "Stok"], tablefmt="double_grid", showindex=False))
    print("")
    print(" [1] Tambah Produk")
    print(" [2] Edit Produk\n")    
    pilih = input("Pilih Menu : ")
    log.clear_terminal()
    match pilih:
        case "1":
            namapd = list(pdProduk["nama"])
            nama = input("Masukkan nama produk : ")
            if nama in namapd or nama == "":
                if nama in namapd:
                    print("Nama produk sudah ada !!")
                elif nama =="":
                    print("Nama produk tidak boleh kosong !! ")
                keluar = input("Tekan enter untuk melanjutkan / n untuk keluar ke menu")
                if keluar == "n":
                    log.clear_terminal()
                    return
                else:
                    tambah_produk()
                    
            harga = int(input("Masukkan harga produk : "))
            stok = int(input("Masukkan stok produk : "))
            if pdProduk.shape[0] == 0:
                newProduk = pd.DataFrame({
                    "id":[1],
                    "nama":[nama],
                    "harga":[harga],
                    "stok":[stok],
                    "view":[1],
                })
                newProduk.to_csv("stok_produk.csv",mode ="a",index=False,header=False)
                print("Produk berhasil ditambahkan")
            else:   
                newProduk = pd.DataFrame({
                "id":[pdProduk.iloc[-1]["id"]+1],
                "nama":[nama],
                "harga":[harga],
                "stok":[stok],
                "view":[1],
                })
                newProduk.to_csv("stok_produk.csv",mode ="a",index=False,header=False)
                print("Produk berhasil ditambahkan")
            input("Tekan enter untuk kembali ke menu")  
            log.clear_terminal()
        case "2":
            # print(pdProduk.to_string(index=False))
            print(tb(pdview, headers=["ID", "Nama Produk", "Harga", "Stok"], tablefmt="double_grid", showindex=False))
            try:
                edit = int(input("Masukkan id produk yang akan diedit : "))
                nama = input("Masukkan nama produk : ")
                harga = int(input("Masukkan harga produk : "))
                stok = int(input("Masukkan stok produk : "))
                pdProduk.loc[pdProduk['id'] == int(edit),['nama','harga',"stok"]] = [nama,harga,stok]
                pdProduk.to_csv("stok_produk.csv",index=False)
                print("Produk berhasil diedit")
            except:
                print("Input tidak valid")
                lanjut = input("Tekan enter untuk Lanjut / ketik n untuk kembali ke menu : ")
                if lanjut != "n":
                    tambah_produk()
                else:
                    return
        case _:
            return

def list_produk():
    while True:
        log.clear_terminal()
        pdProduk = log.cek_file("stok_produk.csv")
        pdview = pdProduk[pdProduk["view"]==1]  
        pdview = pdview.drop(columns=["view"],)

        # print(pdview.to_string(index=False))
        print(tb(pdview, headers=["ID", "Nama Produk", "Harga", "Stok"], tablefmt="double_grid", showindex=False))

        input_lanjut = input("Tekan enter untuk kembali ke menu")
        if input_lanjut == 'y':
            continue
        else:
            return