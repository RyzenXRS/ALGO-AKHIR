import pandas as pd

tanaman = pd.read_csv("list_bibit.csv")

tanaman.index += 1

print("Daftar Tanaman:")
print(tanaman[['Nama Tanaman']])

try:
    input_tanaman = int(input("Pilih nomor tanaman yang kamu mau: "))

    if input_tanaman in tanaman.index:
        print("\nKamu memilih tanaman:", tanaman.iloc[input_tanaman - 1]['Nama Tanaman'])
        
        # Menampilkan detail tanaman yang dipilih
        match_tanaman = tanaman.loc[input_tanaman]
        print("\nDetail Tanaman yang Dipilih:")
        print(f"Nama Tanaman: {match_tanaman['Nama Tanaman']}")
        print(f"Jenis Tanaman: {match_tanaman['Jenis Tanaman']}")
        print(f"Kebutuhan Air: {match_tanaman['Kebutuhan Air']}")
        print(f"Kebutuhan Cahaya: {match_tanaman['Kebutuhan Cahaya']}")
        print(f"Suhu Ideal: {match_tanaman['Suhu Ideal']}")
    else:
        print("Nomor tanaman tidak ditemukan.")
except ValueError:
    print("Input tidak valid, harap masukkan nomor yang benar.")
