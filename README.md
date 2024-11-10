# Latihan1
Menampilkan bilangan (n) acak yang bernilai lebih kecil dari 0.5

---
## Code program 
```python
import random

n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan : "))
random_numbers = []

while len(random_numbers) < n:
    number = random.random()
    if number < 0.5:
        random_numbers.append(number)

print("Bilangan acak yang lebih kecil dari 0.5:")
for num in random_numbers:
    print(num)
print("selesai")
```
---
## Output 
[output](output/latihan1.png)

---
## Penjelasan Program 
1. Input n: Program meminta pengguna untuk memasukkan jumlah bilangan acak yang ingin dihasilkan.
2. while loop: Program menggunakan while loop untuk terus menghasilkan bilangan acak hingga jumlah bilangan acak yang memenuhi syarat (< 0.5) sebanyak sama dengan n.
3. if statement: Setiap kali bilangan acak dihasilkan, program memeriksa apakah bilangan tersebut kurang dari 0.5. Jika benar, bilangan itu ditambahkan ke dalam list random_numbers.
4. Output: Setelah while loop selesai, program menggunakan for loop untuk menampilkan semua bilangan acak yang disimpan dalam list random_numbers.

# Latihan 2 
Menghitung Laba dan keuntungan perusahaan selama 8 bulan 

---
## Code Program 
```python
# Modal awal dalam juta
modal_awal = 100

# Inisialisasi keuntungan total
total_keuntungan = 0

# Loop untuk menghitung keuntungan setiap bulan
for bulan in range(1, 9):  # Mulai dari bulan 1 sampai bulan 8
    if bulan <= 2:
        laba_persen = 0     # Bulan 1 dan 2 belum mendapatkan laba
    elif bulan == 3 or bulan == 4:
        laba_persen = 1     # Bulan 3 dan 4, laba 1%
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba_persen = 5     # Bulan 5, 6, dan 7, laba 5%
    elif bulan == 8:
        laba_persen = 3     # Bulan 8, laba turun menjadi 3%
    
    # Hitung keuntungan bulan ini
    laba_bulan_ini = modal_awal * (laba_persen / 100)
    total_keuntungan += laba_bulan_ini

    # Tampilkan laba per bulan (opsional)
    print(f"Bulan {bulan}: Laba {laba_persen}% = {laba_bulan_ini} juta")

# Tampilkan total keuntungan setelah 8 bulan
print("\nTotal Keuntungan selama 8 bulan:", total_keuntungan, "juta")
```
---
## Output program 
[output](output/latihan2.png)

---
## Penjelasan Program
