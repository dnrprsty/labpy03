saldo = 1000000

print("Selamat datang di Mesin ATM!")
print(f"Saldo awal Anda: Rp {saldo}\n")

while True:
    print("Pilih menu:")
    print("1. Tarik Tunai")
    print("2. Keluar")
    
    pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

    if pilihan == '1':
        jumlah_tarik = int(input("Masukkan jumlah uang yang ingin ditarik: Rp "))

        if jumlah_tarik > saldo:
            print("Maaf, saldo Anda tidak mencukupi.")
        elif jumlah_tarik <= 0:
            print("Jumlah penarikan tidak valid.")
        else:
            saldo -= jumlah_tarik
            print(f"Anda berhasil menarik Rp {jumlah_tarik}. \nSisa saldo Anda: Rp {saldo}")
            
            if saldo == 0:
                print("Saldo Anda habis. Terima kasih telah menggunakan layanan kami.")
                break

    elif pilihan == '2':
        print("Terima kasih telah menggunakan layanan kami.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
