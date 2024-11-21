import pandas as pd

# Membaca file CSV yang berisi data resep
resep = pd.read_csv("list_resep.csv")

# Mengubah index menjadi 1-based (dimulai dari 1, bukan 0)
resep.index += 1

# Menampilkan daftar nama resep dengan nomor
print("Daftar Resep:")
print(resep[['nama_resep']])

# Meminta input dari pengguna berupa angka untuk memilih resep
try:
    input_resep = int(input("Pilih nomor resep yang kamu mau: "))
    
    # Cek apakah input_resap valid (nomor yang dipilih ada dalam index)
    print("Kamu memilih resep:", resep.iloc[input_resep - 1]['nama_resep'])
    if input_resep in resep.index:
        # Menampilkan detail resep yang dipilih
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