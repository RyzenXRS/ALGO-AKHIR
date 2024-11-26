import login as log
def dashboard(user):
    if user[2] == "pembeli":
        print(
    """
    ╔═══════════════════════════╗
    ║       Selamat Datang      ║
    ║┌─────────────────────────┐║
    ║│  1. Login               │║
    ║│  2. Register            │║
    ║│  3. Rekomendasi Resep   │║
    ║│  4. Rekomend Bibit      │║
    ║│  5. Rekomendasi Pupuk   │║
    ║│  6. Keluar              │║
    ║├─────────────────────────┤║
    ║│  Mahasiswa : {user[0]}  │║
    ║└─────────────────────────┘║
    ╚═══════════════════════════╝
    """)
    elif user[2] == "penjual":
        print(
    """
    ╔═══════════════════════════╗
    ║       Selamat Datang      ║
    ║┌─────────────────────────┐║
    ║│  1. Login               │║
    ║│  2. Register            │║
    ║│  3. Tambah Stok         │║
    ║│  4. Riwayat Tranksaksi  │║
    ║│  5. Rekap Penjualan     │║
    ║│  6. Keluar              │║
    ║├─────────────────────────┤║
    ║│  Penjual : {user[0]}  │║
    ║└─────────────────────────┘║
    ╚═══════════════════════════╝
    """)
    elif user[3] == "admin":
        print(
    """
    ╔═══════════════════════════╗
    ║       Selamat Datang      ║
    ║┌─────────────────────────┐║
    ║│  1. Login               │║
    ║│  2. Register            │║
    ║│  3. Tambah Saldo pengguna │║
    ║│  4. Buat voucher diskon │║
    ║│  5. Rekap Penjualan     │║
    ║│  6. Keluar              │║
    ║├─────────────────────────┤║
    ║│  Admin :                │║
    ║└─────────────────────────┘║
    ╚═══════════════════════════╝
    """)