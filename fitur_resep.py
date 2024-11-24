import pandas as pd

 
resep = pd.read_csv("list_resep.csv")


resep.index += 1


print("Daftar Resep:")
print(resep[['nama_resep']])

try:
    input_resep = int(input("Pilih nomor resep yang kamu mau: "))
    
    
    print("Kamu memilih resep:", resep.iloc[input_resep - 1]['nama_resep'])
    if input_resep in resep.index:
        
        match_resep = resep.loc[input_resep]
        for col in match_resep.index:
            print(f"{col}:")
            print(match_resep[col])
            print()
    else:
        print("Nomor resep tidak ditemukan.")
except ValueError:
    print("Input tidak valid, harap masukkan nomor yang benar.")

# # Meminta input untuk melanjutkan atau keluar
# inputan_stop = input("Apakah kamu ingin lanjut [y/t] : ").lower()
# if inputan_stop == 't':
#     menu()  # Panggil menu jika user ingin keluar
# elif inputan_stop == 'y':
#     clear_terminal()  # Bersihkan terminal untuk memulai lagi
#     list_resep()  # Tampilkan daftar resep lagi
# else:
#     print("Tidak ada pilihan!")