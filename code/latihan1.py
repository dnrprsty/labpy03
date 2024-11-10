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
