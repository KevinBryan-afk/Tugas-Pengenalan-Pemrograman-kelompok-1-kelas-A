from fitur_perkalian_dan_pembagian.py import kali,bagi
from fitur_tambah_kurang.py import tambah,kurang
def tampilkan_menu():
  print("Kalkulator Sederhana")
  print("1. Penjumlahan")
  print("2. Pengurangan")
  print("3. Perkalian")
  print("4. Pembagian")

def input_angka()
  a = float(input("angka pertama: "))
  b =  float(input("angka kedua: "))
  return a, b

def main()
  tampilkan_menu()
  
  pilihan = input("Pilih Operasi yang ingin digunakan. (1/2/3/4) ")
  a, b = input_angka()
  
  if pilihan == 1:
    hasil = tambah(a,b)
  elif pilihan == 2:
    hasil = kurang(a,b)
  elif pilihan == 3:
    hasil = kali(a,b)
  elif pilihan == 4:
    hasil = bagi(a,b)
  else:
    print("Pilihan tidak valid!")
    return
  
  print("Hasil:", hasil)

if __name__ == "__main__":
  main()
