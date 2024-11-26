import login as log
import tes as db

def main():
    log.menu_tampilan()
    pilihan = input("Masukkan inputan : ")
    match pilihan:
        case "1":
            user = log.login()
            while log.login_status:
                db.dashboard(user)
                db.pilih_dashboard(user)
        case "2":
            log.buat_akun()
        case "3":
            print("Terima kasih")
        case _:
            print("Pilihan tidak ada")