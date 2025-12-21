Program kalkulator sederhana menggunakan bahasa python

Pendahuluan: 
Program ini merupakan kalkulator sederhana berbasis Python yang dibuat sebagai tugas kelompok. Program ini dapat melakukan operasi hitung dasar melalui menu di terminal dengan struktur kode yang terpisah agar mudah dipahami.

Fitur Utama Terdiri Atas:
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian

Cara menjalankan:
1. Pastikan Python sudah terinstall.
2. Buka Terminal di folder projek.
3. Jalankan: python main.py

Panduan Menjalankan:
1. Buka Terminal / Command Prompt
2. Masuk ke Folder Program
3. Jalankan Program
4. Kalkulator Muncul
5. Masukkan Angka dan Pilih Operasi dan Hasil Perhitungan akan Muncul
6. Tutup Program Setelah Selesai


Dokumentasi Teknis:

'''graph TD
    A([Mulai]) --> B[Tampilkan Menu Operasi]
    B --> C{Pilih Operasi 0-4}
    
    C -- "0" --> L([Keluar])
    C -- "1, 2, 3, 4" --> D[/Input Angka Pertama & Kedua/]
    
    D --> E{Pilihan Operasi?}
    
    E -- "1 (Tambah)" --> F[Panggil fitur_tambah_kurang.py]
    E -- "2 (Kurang)" --> G[Panggil fitur_tambah_kurang.py]
    E -- "3 (Kali)" --> H[Panggil fitur_perkalian_dan_pembagian.py]
    E -- "4 (Bagi)" --> I[Panggil fitur_perkalian_dan_pembagian.py]
    
    F & G & H & I --> J[Proses Perhitungan]
    J --> K[/Tampilkan Hasil/]
    K --> B

'''
