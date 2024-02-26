# Fungsi untuk menghitung jumlah password kuat dengan panjang n
def countStrongPasswords(n):
    if n < 1:
        return 0
    
    # Inisialisasi array DP dengan 2 indeks
    # DP[i][0] akan menyimpan jumlah password kuat yang berakhir dengan angka
    # DP[i][1] akan menyimpan jumlah password kuat yang berakhir dengan karakter yang bukan angka
    DP = [[0, 0] for _ in range(n + 1)]
    
    # Kasus dasar untuk panjang 1
    DP[1][0] = 10  # Angka 0-9
    DP[1][1] = 0   # Tidak ada karakter yang bukan angka
    
    # Iterasi untuk panjang password dari 2 hingga n
    for i in range(2, n + 1):
        # Untuk DP[i][0], kita bisa mengakhiri dengan angka apa saja (0-9), asalkan tidak sama dengan angka sebelumnya (DP[i-1][0])
        DP[i][0] = 10 * DP[i-1][0]
        
        # Untuk DP[i][1], kita bisa mengakhiri dengan karakter yang bukan angka (26 pilihan), karena karakter sebelumnya bisa berupa angka atau karakter yang bukan angka
        DP[i][1] = 26 * (DP[i-1][0] + DP[i-1][1])
    
    # Jumlah total password kuat dengan panjang n adalah DP[n][0] + DP[n][1]
    return DP[n][0] + DP[n][1]

# Panggil fungsi dengan panjang password 6
n = 6
result = countStrongPasswords(n)
print("Jumlah password kuat dengan panjang 6 karakter adalah:", result)
