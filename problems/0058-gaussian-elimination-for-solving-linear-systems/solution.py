import numpy as np

def gaussian_elimination(A, b):
    # Hesaplama hassasiyeti için float'a çeviriyoruz
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    # 1. FAZ: İleriye Doğru Yok Etme + Kısmi Pivotlama
    for i in range(n):
        # --- Partial Pivoting ---
        # i. sütundaki mutlak değerce en büyük elemanın bulunduğu satırı bul
        pivot_row = i + np.argmax(np.abs(A[i:, i]))
        
        # Eğer en büyük eleman şu anki satırda değilse, satırları takas et
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
            b[[i, pivot_row]] = b[[pivot_row, i]]

        # --- Alt Satırları Sıfırlama ---
        for j in range(i + 1, n):
            oran = A[j, i] / A[i, i]
            A[j, i:] -= oran * A[i, i:]
            b[j] -= oran * b[i]

    # 2. FAZ: Geriye Doğru Yerine Koyma (Back-substitution)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        # b[i]'den daha önce bulunan x değerlerinin katkısını çıkar ve köşegene böl
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x.tolist()