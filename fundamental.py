
import time
print("\n====== aplikasi kuis sederhana =======")



print("1. kuis matematika")
print("2. kuis bahasa indonesia")




skor = []


def kuis_matemtika():
    print("\n====================================")
    print("Soal 1: Berapa nilai x dari persamaan 4x + 7 = 31?")
    print(" A. x = 5 B. x = 6 C. x = 7")
    print("\n====================================")
    
def next_soalmatetika():
    
    print("\n==================================")
    print("Soal 2: Berapa hasil dari 12 * 3?")
    print(" A. 36 B. 32 C. 30")
    print("\n==================================")
    
    
    
    
while True:
    user = int(input("masukan pilihan kuis anda :")) 
   
    if user == 1:
        kuis_matemtika()
        hasil_hitung = (input("masukan jawaban anda :"))
        
        if hasil_hitung == "B":
            time.sleep(2)
            print("jawaban anda benar ✅🏆")
            skor.append(10)
                
            print("skor anda ", skor)
            ## pilihan lanjut 
            time.sleep(2)
            next = input("apakah anda ingin melanjutkan ke soal berikutnya? (y/n) :")
            
            
                
            while True:    
                if next == "y":
                    next_soalmatetika()
                
                
                    hasil = (input("masukan jawaban anda :"))
                    
                    
                    
                        
                    if hasil == "A":
                        print("jawban anda benar 🤩🤩 ")
                        skor[0] = 20
                        print("skor anda sekarang 🏆", skor)
                        
                        break
                    elif hasil == "B" and "C":
                        print("maaf jawaban anda salah 😭😭")
                        
                    else:
                        print("jawaban tidak boleh kosong tolong masukan jawaban and")
            
        else:
            print("jawaban anda salah")
            break
            
    elif user == 2:
        print("soal belum tersedia")
        
    else:
        print("pilihan tidak valid tolong isi ulang")
        continue

    
## sko