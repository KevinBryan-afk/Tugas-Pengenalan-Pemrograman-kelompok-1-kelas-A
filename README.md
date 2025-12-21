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

flowchart TD
    A([Mulai]) --> B[Tampilkan Menu Operasi]
    B --> C{Pilihan Pengguna?}
    
    C -- "0" --> D([Selesai])
    C -- "1, 2, 3, 4" --> E[/Input Dua Angka/]
    
    E --> F{Jenis Operasi?}
    
    F -- "1 atau 2" --> G[Proses di Modul fitur_tambah_kurang]
    F -- "3 atau 4" --> H[Proses di Modul fitur_perkalian_dan_pembagian]
    
    G --> I[/Tampilkan Hasil/]
    H --> I
    I --> B
