import random

def permainan_tebak_angka():
    while True:
        angka_rahasia = random.randint(1, 50)
        kesempatan = 5
        print("\nBOT sudah memilih angka antara 1 sampai 50.")
        print("Ayo tebak!")

        while kesempatan > 0:
            try:
                tebakan = int(input("Masukkan tebakan Anda: "))
            except ValueError:
                print("Harap masukkan angka yang valid!")
                continue

            if tebakan < angka_rahasia:
                print("Bilangan lebih besar!")
            elif tebakan > angka_rahasia:
                print("Bilangan lebih kecil!")
            else:
                print("Jawaban Anda benar 🎉")
                break
            kesempatan -= 1
            if kesempatan > 0:
                print(f"Sisa nyawa: {kesempatan}")
            else:
                print(f"Nyawa anda habis! Angka rahasia adalah {angka_rahasia}")

        # Tanya apakah ingin mengulang
        ulang = input("Apakah Anda ingin mengulang permainan? (y/n): ").lower()
        if ulang != 'y':
            print("Terima kasih sudah bermain!")
            break

# Jalankan permainan 
if __name__ == "__main__":

    permainan_tebak_angka()
