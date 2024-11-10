modal_awal = 100

total_keuntungan = 0

for bulan in range(1, 9):  
    if bulan <= 2:
        laba_persen = 0     
    elif bulan == 3 or bulan == 4:
        laba_persen = 1   
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba_persen = 5    
    elif bulan == 8:
        laba_persen = 3     
  
    laba_bulan_ini = modal_awal * (laba_persen / 100)
    total_keuntungan += laba_bulan_ini

    print(f"Bulan {bulan}: Laba {laba_persen}% = {laba_bulan_ini} juta")

print("\nTotal Keuntungan selama 8 bulan:", total_keuntungan, "juta")
