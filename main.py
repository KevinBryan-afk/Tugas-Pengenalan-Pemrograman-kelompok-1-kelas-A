from fitur_perkalian_dan_pembagian import kali,bagi
from fitur_tambah_kurang import tambah,kurang
def tampilkan_menu():
  print("Kalkulator Sederhana")
  print("1. Penjumlahan")
  print("2. Pengurangan")
  print("3. Perkalian")
  print("4. Pembagian")

def input_angka():
  a = float(input("angka pertama: "))
  b = float(input("angka kedua: "))
  return a, b

def main():
  while True:
    tampilkan_menu() 
    pilihan = input("Pilih operasi (0/1/2/3/4): ")
    if pilihan == "0":
     print("Program dihentikan.")
     break
     
    if pilihan not in ("1", "2", "3", "4"):
       print("Pilihan tidak valid.")
       continue


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
