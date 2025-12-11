"""
PROYEK ALJABAR DAN MATRIKS
Bagian 1: Implementasi Operasi Matriks
Kelompok: 1
Anggota:
1. [Muhammad Vigar Septianta Pratama] - [240602010]
2. [Andika Eka Putra Yulianto] - [240602021]
3. [Muhammad Zaki Azhari] - [240602023]
4. [Rohmah Nur Hidayah] - [240602026]
"""

import numpy as np

print("="*70)
print("BAGIAN 1: IMPLEMENTASI OPERASI MATRIKS")
print("="*70)

# =======================================================================
# 1. Operasi dasar matriks (pakai NumPy biar cepat)
# =======================================================================

print("\n" + "="*70)
print("1. OPERASI DASAR MATRIKS (NumPy)")
print("="*70)

# Contoh dua matriks 3x3 yang akan dipakai
A = np.array([[4, 3, 2],
              [1, 5, 3],
              [2, 1, 6]])

B = np.array([[2, 1, 4],
              [3, 2, 1],
              [1, 3, 2]])

print("\n--- Matriks Input ---")
print("Matriks A:")
print(A)
print("\nMatriks B:")
print(B)

# a. Penjumlahan matriks
print("\n--- a. Penjumlahan Matriks ---")
C_sum = A + B
print("A + B =")
print(C_sum)
print("Keterangan: elemen dijumlahkan satu-satu sesuai posisi.")

# b. Pengurangan matriks
print("\n--- b. Pengurangan Matriks ---")
C_sub = A - B
print("A - B =")
print(C_sub)
print("Keterangan: prinsipnya sama kaya penjumlahan, cuma dikurang.")

# c. Perkalian matriks
print("\n--- c. Perkalian Matriks ---")
C_mul = A @ B
print("A × B =")
print(C_mul)
print("Keterangan: ini pakai aturan baris ketemu kolom.")

# d. Determinan
print("\n--- d. Determinan Matriks ---")
detA = np.linalg.det(A)
detB = np.linalg.det(B)
print(f"det(A) = {detA:.2f}")
print(f"det(B) = {detB:.2f}")
print("Keterangan: kalau determinan ≠ 0 berarti ada inversnya.")

# e. Invers Matriks
print("\n--- e. Invers Matriks ---")
if detA != 0:
    A_inv = np.linalg.inv(A)
    print("Invers A:")
    print(A_inv)

    print("\nCek A × A⁻¹:")
    print(A @ A_inv)
else:
    print("A tidak punya invers (det = 0).")

# =======================================================================
# 2. Fungsi manual untuk perkalian matriks (tanpa NumPy high-level)
# =======================================================================

print("\n\n" + "="*70)
print("2. PERKALIAN MATRIKS MANUAL")
print("="*70)

def matmul_manual(X, Y):
    """
    Perkalian matriks manual.
    Intinya cuma pakai rumus Σ (baris X * kolom Y)
    """
    m, n = X.shape
    n2, p = Y.shape

    # ngecek apakah jumlah kolom X = jumlah baris Y
    assert n == n2, "Ukuran matriks tidak kompatibel."

    Z = np.zeros((m, p))

    # 3 loop klasik perkalian matriks
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += X[i, k] * Y[k, j]
            Z[i, j] = total
    return Z

# Test Case 1
print("\n--- Test Case 1 (2x2) ---")
M1 = np.array([[1, 2],
               [3, 4]])
M2 = np.array([[5, 6],
               [7, 8]])

print("M1 =")
print(M1)
print("\nM2 =")
print(M2)

hasil_manual = matmul_manual(M1, M2)
print("\nHasil Manual =")
print(hasil_manual)

hasil_numpy = M1 @ M2
print("\nHasil NumPy =")
print(hasil_numpy)
print("Cocok?", np.allclose(hasil_manual, hasil_numpy))

# =======================================================================
# 3. Eliminasi Gauss (manual)
# =======================================================================

print("\n\n" + "="*70)
print("3. ELIMINASI GAUSS")
print("="*70)

def gauss_elimination(aug):
    """
    Eliminasi Gauss sederhana.
    aug = matriks augmented [A|b].
    """
    aug = aug.astype(float)
    row, col = aug.shape
    n = col - 1   # jumlah variabel

    # Tahap forward elimination
    for i in range(n):
        # mencari pivot terbesar (biar lebih stabil)
        pivot_row = i
        for r in range(i+1, row):
            if abs(aug[r, i]) > abs(aug[pivot_row, i]):
                pivot_row = r

        # tukar baris kalau perlu
        aug[[i, pivot_row]] = aug[[pivot_row, i]]

        pivot = aug[i, i]
        if abs(pivot) < 1e-10:
            raise ValueError("Pivot terlalu kecil, kemungkinan singular.")

        # normalisasi baris pivot
        aug[i] = aug[i] / pivot

        # eliminasi baris di bawahnya
        for r in range(i+1, row):
            factor = aug[r, i]
            aug[r] -= factor * aug[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = aug[i, -1] - np.dot(aug[i, i+1:n], x[i+1:n])

    return x

# Test Case 1
print("\n--- SPL 2 Variabel ---")
print("2x + y = 5")
print("4x + 3y = 11")

aug1 = np.array([[2., 1., 5.],
                 [4., 3., 11.]])

sol1 = gauss_elimination(aug1.copy())
print("Solusi:", sol1)

# Test Case 2
print("\n--- SPL 3 Variabel ---")

aug2 = np.array([[2., 1., -1., 8.],
                 [-3., -1., 2., -11.],
                 [-2., 1., 2., -3.]])

sol2 = gauss_elimination(aug2.copy())
print("Solusi:", sol2)

# Test Case 3
print("\n--- SPL 4 Variabel ---")

aug3 = np.array([[1., 2., 3., 1., 10.],
                 [2., 1., 2., 3., 13.],
                 [3., 2., 1., 2., 12.],
                 [4., 3., 2., 1., 15.]])

sol3 = gauss_elimination(aug3.copy())
print("Solusi:", sol3)

print("\n" + "="*70)
print("BAGIAN 1 SELESAI")
print("="*70)