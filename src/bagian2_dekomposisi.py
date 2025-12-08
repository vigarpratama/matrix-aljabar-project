"""
PROYEK ALJABAR DAN MATRIKS
Bagian 2: Dekomposisi Matriks (LU, QR, Eigenvalue-Eigenvector)
"""

import numpy as np
from scipy.linalg import lu, qr

print("="*70)
print("BAGIAN 2: DEKOMPOSISI MATRIKS")
print("="*70)

# ============================================================================
# 1. DEKOMPOSISI LU
# ============================================================================

print("\n" + "="*70)
print("1. DEKOMPOSISI LU")
print("="*70)

print("\nDekomposisi LU memecah matriks A menjadi:")
print("A = P × L × U")
print("- P: Permutation matrix")
print("- L: Lower triangular matrix")
print("- U: Upper triangular matrix")

# Matriks 4×4
A = np.array([[4., 3., 2., 1.],
              [1., 5., 3., 2.],
              [2., 1., 6., 3.],
              [1., 2., 3., 7.]], dtype=float)

print("\n--- Matriks A (4×4) ---")
print(A)

# Dekomposisi LU menggunakan scipy
P, L, U = lu(A)

print("\n--- Hasil Dekomposisi LU ---")
print("\nMatriks P (Permutation):")
print(P)

print("\nMatriks L (Lower Triangular):")
print(L)

print("\nMatriks U (Upper Triangular):")
print(U)

# Verifikasi: P × L × U = A
reconstructed = P @ L @ U
print("\n--- Verifikasi: P × L × U = A ---")
print("P × L × U =")
print(reconstructed)

print("\nMatriks A (original):")
print(A)

print(f"\nApakah P×L×U = A? {np.allclose(reconstructed, A)}")
print(f"Maksimum error: {np.max(np.abs(reconstructed - A)):.2e}")

# Aplikasi: Menyelesaikan SPL Ax = b menggunakan LU
print("\n--- Aplikasi: Menyelesaikan SPL dengan LU ---")
b = np.array([10., 15., 20., 25.])
print(f"Vektor b: {b}")

# Langkah 1: P × A × x = P × b → L × U × x = P × b
Pb = P @ b

# Langkah 2: Solve L × y = P × b (forward substitution)
y = np.linalg.solve(L, Pb)

# Langkah 3: Solve U × x = y (backward substitution)
x = np.linalg.solve(U, y)

print(f"\nSolusi x: {x}")

# Verifikasi
verif = A @ x
print(f"Verifikasi A×x: {verif}")
print(f"b: {b}")
print(f"Benar? {np.allclose(verif, b)}")

# ============================================================================
# 2. DEKOMPOSISI QR
# ============================================================================

print("\n\n" + "="*70)
print("2. DEKOMPOSISI QR")
print("="*70)

print("\nDekomposisi QR memecah matriks A menjadi:")
print("A = Q × R")
print("- Q: Orthogonal matrix (Q^T × Q = I)")
print("- R: Upper triangular matrix")

# Matriks 4×4
B = np.array([[12., 6., -4., 2.],
              [-51., 167., 24., 8.],
              [4., -68., -41., 10.],
              [2., 3., 5., 15.]], dtype=float)

print("\n--- Matriks B (4×4) ---")
print(B)

# Dekomposisi QR
Q, R = qr(B)

print("\n--- Hasil Dekomposisi QR ---")
print("\nMatriks Q (Orthogonal):")
print(Q)

print("\nMatriks R (Upper Triangular):")
print(R)

# Verifikasi 1: Q × R = B
reconstructed_qr = Q @ R
print("\n--- Verifikasi 1: Q × R = B ---")
print("Q × R =")
print(reconstructed_qr)

print("\nMatriks B (original):")
print(B)

print(f"\nApakah Q×R = B? {np.allclose(reconstructed_qr, B)}")
print(f"Maksimum error: {np.max(np.abs(reconstructed_qr - B)):.2e}")

# Verifikasi 2: Q^T × Q = I (Q orthogonal)
QTQ = Q.T @ Q
print("\n--- Verifikasi 2: Q^T × Q = I ---")
print("Q^T × Q =")
print(QTQ)

print("\nIdentity Matrix I:")
I = np.eye(4)
print(I)

print(f"\nApakah Q^T×Q = I? {np.allclose(QTQ, I)}")
print(f"Maksimum error: {np.max(np.abs(QTQ - I)):.2e}")

# Aplikasi: Least Squares dengan QR
print("\n--- Aplikasi: Least Squares Problem ---")
print("Mencari solusi x yang meminimalkan ||Bx - c||")

c = np.array([10., 20., 30., 40.])
print(f"Vektor c: {c}")

# Solusi: x = R^(-1) × Q^T × c
QTc = Q.T @ c
x_ls = np.linalg.solve(R, QTc)

print(f"\nSolusi least squares x: {x_ls}")

# Verifikasi
residual = B @ x_ls - c
print(f"Residual B×x - c: {residual}")
print(f"Norm residual: {np.linalg.norm(residual):.6f}")

# ============================================================================
# 3. EIGENVALUE dan EIGENVECTOR
# ============================================================================

print("\n\n" + "="*70)
print("3. EIGENVALUE dan EIGENVECTOR")
print("="*70)

print("\nEigenvalue λ dan eigenvector v memenuhi:")
print("A × v = λ × v")

# Matriks simetris 4×4 (eigenvalue real)
C = np.array([[4., 2., 1., 0.],
              [2., 5., 3., 1.],
              [1., 3., 6., 2.],
              [0., 1., 2., 3.]], dtype=float)

print("\n--- Matriks C (4×4, Simetris) ---")
print(C)

# Hitung eigenvalue dan eigenvector
eig_vals, eig_vecs = np.linalg.eig(C)

print("\n--- Eigenvalues ---")
for i, val in enumerate(eig_vals):
    print(f"λ_{i+1} = {val:.6f}")

print("\n--- Eigenvectors ---")
print("(Setiap kolom adalah satu eigenvector)")
print(eig_vecs)

# Verifikasi untuk setiap eigenpair
print("\n--- Verifikasi: A × v_i = λ_i × v_i ---")
for i in range(len(eig_vals)):
    v = eig_vecs[:, i]
    lambda_i = eig_vals[i]
    
    left = C @ v  # A × v
    right = lambda_i * v  # λ × v
    
    print(f"\nEigenpair {i+1}:")
    print(f"λ_{i+1} = {lambda_i:.6f}")
    print(f"v_{i+1} = {v}")
    print(f"A × v_{i+1} = {left}")
    print(f"λ_{i+1} × v_{i+1} = {right}")
    print(f"Sama? {np.allclose(left, right)}")
    print(f"Error: {np.linalg.norm(left - right):.2e}")

# Diagonalisasi: A = V × D × V^(-1)
print("\n--- Diagonalisasi: C = V × D × V^(-1) ---")

# D adalah diagonal matrix dari eigenvalues
D = np.diag(eig_vals)
print("\nMatriks D (Diagonal dari eigenvalues):")
print(D)

# V adalah matrix dari eigenvectors
V = eig_vecs
print("\nMatriks V (Eigenvectors):")
print(V)

# Verifikasi: V × D × V^(-1) = C
V_inv = np.linalg.inv(V)
reconstructed_eig = V @ D @ V_inv

print("\nV × D × V^(-1) =")
print(reconstructed_eig)

print("\nMatriks C (original):")
print(C)

print(f"\nApakah V×D×V^(-1) = C? {np.allclose(reconstructed_eig, C)}")
print(f"Maksimum error: {np.max(np.abs(reconstructed_eig - C)):.2e}")

# Aplikasi: Matrix Power menggunakan eigendecomposition
print("\n--- Aplikasi: Menghitung C^10 dengan Eigendecomposition ---")

# C^n = V × D^n × V^(-1)
n = 10
D_n = np.diag(eig_vals ** n)
C_power = V @ D_n @ V_inv

print(f"\nC^{n} (menggunakan eigendecomposition):")
print(C_power)

# Verifikasi dengan cara langsung
C_power_direct = np.linalg.matrix_power(C, n)
print(f"\nC^{n} (perhitungan langsung):")
print(C_power_direct)

print(f"\nHasil sama? {np.allclose(C_power, C_power_direct)}")
print(f"Maksimum error: {np.max(np.abs(C_power - C_power_direct)):.2e}")

print("\n" + "="*70)
print("BAGIAN 2 SELESAI")
print("="*70)

