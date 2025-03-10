def min_cost_assignment(cost_matrix):
    """
    Müşteri destek temsilcisi yönlendirme algoritması
    Dinamik programlama kullanılarak müşteri-temsilci atamasında minimum maliyet hesaplanır.
    """
    n, m = len(cost_matrix), len(cost_matrix[0])  # n: müşteri sayısı, m: temsilci sayısı
    dp = [[float('inf')] * m for _ in range(n)]  # DP tablosu
    
    # İlk müşteri için her temsilciye atanma maliyetlerini belirle
    for j in range(m):
        dp[0][j] = cost_matrix[0][j]
    
    # Dinamik Programlama ile DP tablosunu güncelleme
    for i in range(1, n):
        for j in range(m):
            dp[i][j] = min(dp[i-1][k] + cost_matrix[i][j] for k in range(m))
    
    # Son müşteriye ait en düşük maliyeti döndür
    return min(dp[n-1])

# Örnek maliyet matrisi (müşteri x temsilci)
cost_matrix = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

# Algoritmayı çalıştır ve sonucu yazdır
print("En düşük toplam maliyet:", min_cost_assignment(cost_matrix))
