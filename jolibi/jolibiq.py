# Langkah 1: Buat himpunan S yang berisi semua bilangan prima kurang dari 200
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

S = [x for x in range(2, 200) if is_prime(x)]

# Langkah 2: Hitung jumlah himpunan bagian dari S
total_sum = 0
for i in range(1, 2**len(S)):
    subset = [S[j] for j in range(len(S)) if (i & (1 << j)) > 0]  # Membuat himpunan bagian
    f_s0 = sum(subset)  # Langkah 3: Hitung f(S0)
    total_sum += f_s0

# Langkah 4: Tampilkan hasil total
print(total_sum)
