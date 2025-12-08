import networkx as nx
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

# ============================================================================
# 1. PEMBUATAN GRAF DAN MATRIKS ADJACENCY
# ============================================================================

print("\n" + "="*70)
print("ANALISIS STRUKTUR JARINGAN SOSIAL MEDIA DALAM LINGKUNGAN KAMPUS")
print("="*70)

# Bikin graf jaringan mahasiswa
G = nx.Graph()

# Nambahin node (mahasiswa)
mahasiswa = ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Henry']
G.add_nodes_from(mahasiswa)

# Nambahin edges (koneksi antar mahasiswa) sesuai matriks adjacency
koneksi = [
    ('Alice', 'Bob'), ('Alice', 'Carol'), ('Alice', 'Eve'),
    ('Bob', 'Carol'), ('Bob', 'David'),
    ('Carol', 'David'), ('Carol', 'Frank'),
    ('David', 'Eve'), ('David', 'Grace'),
    ('Eve', 'Frank'), ('Eve', 'Grace'), ('Eve', 'Henry'),
    ('Frank', 'Grace'),
    ('Grace', 'Henry')
]
G.add_edges_from(koneksi)

print("\n--- Matriks Adjacency ---")
adj_matrix = nx.adjacency_matrix(G, nodelist=mahasiswa).toarray()
print("     ", "  ".join([f"{i}" for i in range(8)]))
for i, nama in enumerate(mahasiswa):
    print(f"{i}: {adj_matrix[i]}  {nama}")

# ============================================================================
# 2. ANALISIS DASAR GRAF
# ============================================================================

print("\n" + "="*70)
print("2. ANALISIS DASAR GRAF")
print("="*70)

print("\n--- a) Degree (Jumlah Koneksi Pertemanan) ---")
degrees = dict(G.degree())
for nama in mahasiswa:
    print(f"{nama:<7}: {degrees[nama]} teman")

max_degree = max(degrees.values())
max_nodes = [k for k, v in degrees.items() if v == max_degree]
print(f"\nMahasiswa dengan popularitas tertinggi: {max_nodes[0]} ({max_degree} teman)")

print("\n--- b) Statistik Karakteristik Graf ---")
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
max_edges = (num_nodes * (num_nodes - 1)) // 2
density = nx.density(G)

print(f"Jumlah total node: {num_nodes}")
print(f"Jumlah total edge: {num_edges}")
print(f"Jumlah edge maksimum yang mungkin: {max_edges}")
print(f"Density: {density:.4f} ({density*100:.2f}%)")
print(f"Kategori: Graf dengan tingkat density yang cukup tinggi")

# ============================================================================
# 3. ANALISIS JALUR DAN KONEKTIVITAS
# ============================================================================

print("\n" + "="*70)
print("3. ANALISIS JALUR DAN KONEKTIVITAS")
print("="*70)

print("\n--- Jalur dengan Panjang 2 (A²) ---")
A2 = np.linalg.matrix_power(adj_matrix, 2)
alice_idx = 0
david_idx = 3
print(f"A²[0,3] = {A2[alice_idx, david_idx]}")
print(f"Terdapat {A2[alice_idx, david_idx]} jalur dari Alice ke David")
print("Jalur: Alice → Bob → David")
print("       Alice → Carol → David")

print("\n--- Jalur dengan Panjang 3 (A³) ---")
A3 = np.linalg.matrix_power(adj_matrix, 3)
henry_idx = 7
print(f"A³[0,7] = {A3[alice_idx, henry_idx]}")
print(f"Terdapat {A3[alice_idx, henry_idx]} jalur berbeda dengan panjang 3 dari Alice ke Henry")

# ============================================================================
# 4. GRAF BERBOBOT (WEIGHTED GRAPH)
# ============================================================================

print("\n" + "="*70)
print("4. GRAF BERBOBOT (WEIGHTED GRAPH)")
print("="*70)

# Bikin graf berbobot
G_weighted = nx.Graph()
G_weighted.add_nodes_from(mahasiswa)

# Nambahin edges dengan bobot (intensitas interaksi)
weighted_edges = [
    ('Alice', 'Bob', 15), ('Alice', 'Carol', 8), ('Alice', 'Eve', 12),
    ('Bob', 'Carol', 20), ('Bob', 'David', 10),
    ('Carol', 'David', 18), ('Carol', 'Frank', 5),
    ('David', 'Eve', 25), ('David', 'Grace', 7),
    ('Eve', 'Frank', 30), ('Eve', 'Grace', 22), ('Eve', 'Henry', 15),
    ('Frank', 'Grace', 12),
    ('Grace', 'Henry', 20)
]
G_weighted.add_weighted_edges_from(weighted_edges)

print("\n--- Jumlah Total Interaksi per Mahasiswa ---")
weighted_degrees = {}
for nama in mahasiswa:
    total = sum([data['weight'] for _, _, data in G_weighted.edges(nama, data=True)])
    weighted_degrees[nama] = total
    print(f"{nama:<7}: {total} pesan/minggu")

max_activity = max(weighted_degrees.values())
max_active = [k for k, v in weighted_degrees.items() if v == max_activity]
print(f"\nMahasiswa dengan aktivitas tertinggi: {max_active[0]} ({max_activity} pesan/minggu)")

print("\nHubungan Pertemanan dengan Intensitas Tertinggi:")
max_weight = max([data['weight'] for _, _, data in G_weighted.edges(data=True)])
for u, v, data in G_weighted.edges(data=True):
    if data['weight'] == max_weight:
        print(f"{u} ↔ {v}: {data['weight']} pesan/minggu")

# ============================================================================
# 5. ALGORITMA SHORTEST PATH (DIJKSTRA)
# ============================================================================

print("\n" + "="*70)
print("5. ALGORITMA SHORTEST PATH (DIJKSTRA)")
print("="*70)

# Konversi bobot ke waktu relatif (berbanding terbalik)
G_time = nx.Graph()
G_time.add_nodes_from(mahasiswa)
for u, v, data in G_weighted.edges(data=True):
    waktu = 1.0 / data['weight']
    G_time.add_edge(u, v, weight=waktu)

print("\nSkenario: Jalur optimal penyampaian informasi dari Alice ke Henry")
path = nx.shortest_path(G_time, 'Alice', 'Henry', weight='weight')
path_length = nx.shortest_path_length(G_time, 'Alice', 'Henry', weight='weight')

print(f"\nJalur Optimal: Alice → Henry")
print(f"Rute: {' → '.join(path)}")
print(f"\nDetail Perhitungan:")
for i in range(len(path)-1):
    weight = G_weighted[path[i]][path[i+1]]['weight']
    waktu = 1.0 / weight
    print(f"  {path[i]} → {path[i+1]}: {weight} pesan/minggu, waktu relatif = {waktu:.4f}")
print(f"\nAkumulasi waktu relatif total: {path_length:.4f}")

# ============================================================================
# 6. ANALISIS CENTRALITY
# ============================================================================

print("\n" + "="*70)
print("6. ANALISIS CENTRALITY")
print("="*70)

# a) Degree Centrality
print("\n--- a) Degree Centrality ---")
degree_cent = nx.degree_centrality(G)
for nama in mahasiswa:
    marker = " (Nilai Tertinggi)" if degree_cent[nama] == max(degree_cent.values()) else ""
    print(f"{nama:<7}: {degree_cent[nama]:.4f}{marker}")

# b) Eigenvector Centrality
print("\n--- b) Eigenvector Centrality ---")
eigen_cent = nx.eigenvector_centrality(G, max_iter=1000)
sorted_eigen = sorted(eigen_cent.items(), key=lambda x: x[1], reverse=True)

for nama in mahasiswa:
    marker = " (Nilai Tertinggi)" if eigen_cent[nama] == max(eigen_cent.values()) else ""
    print(f"{nama:<7}: {eigen_cent[nama]:.4f}{marker}")

print(f"\nMahasiswa dengan pengaruh tertinggi: {sorted_eigen[0][0]}")
print("Interpretasi: Eve memiliki nilai eigenvector centrality tertinggi yang")
print("mengindikasikan bahwa ia bukan hanya memiliki banyak koneksi, tetapi juga")
print("terhubung dengan individu-individu yang memiliki pengaruh signifikan.")

# c) Closeness Centrality
print("\n--- c) Closeness Centrality ---")
closeness_cent = nx.closeness_centrality(G)
for nama in mahasiswa:
    marker = " (Nilai Tertinggi)" if closeness_cent[nama] == max(closeness_cent.values()) else ""
    print(f"{nama:<7}: {closeness_cent[nama]:.4f}{marker}")

# ============================================================================
# 7. DETEKSI KOMUNITAS (SPECTRAL CLUSTERING)
# ============================================================================

print("\n" + "="*70)
print("7. DETEKSI KOMUNITAS (SPECTRAL CLUSTERING)")
print("="*70)

# Hitung matriks Laplacian
L = nx.laplacian_matrix(G, nodelist=mahasiswa).toarray()

print("\n--- Matriks Laplacian: L = D - A ---")

# Hitung eigenvalues dan eigenvectors
eigenvalues, eigenvectors = LA.eigh(L)

print("\n--- Nilai Eigenvalue dari Laplacian ---")
for i, val in enumerate(eigenvalues, 1):
    if i == 1:
        print(f"λ{i} = {val:.6f} (selalu bernilai 0 untuk graf yang terhubung)")
    elif i == 2:
        print(f"λ{i} = {val:.6f} (Algebraic Connectivity)")
    else:
        print(f"λ{i} = {val:.6f}")

algebraic_connectivity = eigenvalues[1]
print(f"\nAlgebraic Connectivity (λ₂): {algebraic_connectivity:.4f}")
print("1. Mengukur tingkat konektivitas dari graf")
print("2. Nilai lebih dari 0 menandakan graf terhubung")
print("3. Nilai yang lebih besar mengindikasikan konektivitas yang lebih kuat")

# Fiedler vector (eigenvector kedua)
fiedler_vector = eigenvectors[:, 1]

print("\n--- Fiedler Vector (untuk Proses Clustering) ---")
for i, nama in enumerate(mahasiswa):
    print(f"{nama:<7}: {fiedler_vector[i]:>8.4f}")

# Deteksi komunitas berdasarkan tanda Fiedler vector
print("\n--- Hasil Deteksi Komunitas (2 kelompok) ---")
kelompok1 = [mahasiswa[i] for i in range(len(mahasiswa)) if fiedler_vector[i] < 0]
kelompok2 = [mahasiswa[i] for i in range(len(mahasiswa)) if fiedler_vector[i] >= 0]

print(f"Kelompok 1: {', '.join(kelompok1)}")
print(f"Kelompok 2: {', '.join(kelompok2)}")

print("\nInterpretasi:")
print("1. Kelompok 1: Terdiri dari mahasiswa dengan nilai Fiedler negatif")
print("2. Kelompok 2: Terdiri dari mahasiswa dengan nilai Fiedler positif")
print("3. Pembagian ini menunjukkan keberadaan dua sub-kelompok yang berbeda")
print("   dalam struktur jaringan sosial")

# ============================================================================
# BONUS: Deteksi Komunitas dengan Greedy Modularity
# ============================================================================

print("\n" + "="*70)
print("BONUS: DETEKSI KOMUNITAS (GREEDY MODULARITY)")
print("="*70)

from networkx.algorithms import community

# Jalanin greedy modularity communities
komunitas = community.greedy_modularity_communities(G)

print(f"\n--- Deteksi Komunitas ({len(komunitas)} clusters) ---")
for idx, cluster in enumerate(komunitas, 1):
    anggota = sorted(list(cluster))
    print(f"Cluster {idx}: {', '.join(anggota)}")

print("\n" + "="*70)
print("ANALISIS SELESAI")
print("="*70)