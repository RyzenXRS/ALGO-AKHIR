def list_resep():
    while True:
        resep = pd.read_csv("list_resep.csv")

        resep.index += 1
        print(resep[['nama_resep']])

        input_resep = input("Resep mana yang kamu mau ? ").lower()

        match_resep = resep[resep['nama_resep'].str.lower() == input_resep]
        
        if not match_resep.empty:
            for col in match_resep.columns:
                print(f"{col}:")
                print(match_resep[col].values[0])
                print()
        else:
            print("Resep tidak ditemukan")

        inputan_stop = input("Apakah kamu ingin lanjut [y/t] : ").lower()
        if inputan_stop == 't':
            menu()
            break
        elif inputan_stop == 'y':
            clear_terminal()
            list_resep()
        else:
            print("Tidak ada pilihan !")
