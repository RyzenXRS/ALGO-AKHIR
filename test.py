import pandas as pd

def list_resep():
    resep = pd.read_csv("list_resep.csv")

    resep.index += 1
    print(resep[['nama_resep']])

    input_resep = input("Resep mana yang kamu mau ? ").lower()

    match_resep = resep[resep['nama_resep'].str.lower() == input_resep]
    
    if not match_resep.empty:
        # Menampilkan setiap kolom dengan cara vertikal
        for col in match_resep.columns:
            print(f"{col}:")
            print(match_resep[col].values[0])
            print()  # Untuk memberi jarak antar kolom
    else:
        print("Resep tidak ditemukan")

list_resep()
