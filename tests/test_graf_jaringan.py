# ======================================================================
# ANALISIS STRUKTUR JARINGAN SOSIAL MEDIA DALAM LINGKUNGAN KAMPUS
# ======================================================================
# 
# --- Matriks Adjacency ---
#       0  1  2  3  4  5  6  7
# 0: [0 1 1 0 1 0 0 0]  Alice
# 1: [1 0 1 1 0 0 0 0]  Bob
# 2: [1 1 0 1 0 1 0 0]  Carol
# 3: [0 1 1 0 1 0 1 0]  David
# 4: [1 0 0 1 0 1 1 1]  Eve
# 5: [0 0 1 0 1 0 1 0]  Frank
# 6: [0 0 0 1 1 1 0 1]  Grace
# 7: [0 0 0 0 1 0 1 0]  Henry
# 
# ======================================================================
# 2. ANALISIS DASAR GRAF
# ======================================================================
# 
# --- a) Degree (Jumlah Koneksi Pertemanan) ---
# Alice  : 3 teman
# Bob    : 3 teman
# Carol  : 4 teman
# David  : 4 teman
# Eve    : 5 teman
# Frank  : 3 teman
# Grace  : 4 teman
# Henry  : 2 teman
# 
# Mahasiswa dengan popularitas tertinggi: Eve (5 teman)
# 
# --- b) Statistik Karakteristik Graf ---
# Jumlah total node: 8
# Jumlah total edge: 14
# Jumlah edge maksimum yang mungkin: 28
# Density: 0.5000 (50.00%)
# Kategori: Graf dengan tingkat density yang cukup tinggi
# 
# ======================================================================
# 3. ANALISIS JALUR DAN KONEKTIVITAS
# ======================================================================
# 
# --- Jalur dengan Panjang 2 (A²) ---
# A²[0,3] = 2
# Terdapat 2 jalur dari Alice ke David
# Jalur: Alice → Bob → David
#        Alice → Carol → David
# 
# --- Jalur dengan Panjang 3 (A³) ---
# A³[0,7] = 4
# Terdapat 4 jalur berbeda dengan panjang 3 dari Alice ke Henry
# 
# ======================================================================
# 4. GRAF BERBOBOT (WEIGHTED GRAPH)
# ======================================================================
# 
# --- Jumlah Total Interaksi per Mahasiswa ---
# Alice  : 35 pesan/minggu
# Bob    : 45 pesan/minggu
# Carol  : 51 pesan/minggu
# David  : 60 pesan/minggu
# Eve    : 104 pesan/minggu
# Frank  : 47 pesan/minggu
# Grace  : 61 pesan/minggu
# Henry  : 35 pesan/minggu
# 
# Mahasiswa dengan aktivitas tertinggi: Eve (104 pesan/minggu)
# 
# Hubungan Pertemanan dengan Intensitas Tertinggi:
# Eve ↔ Frank: 30 pesan/minggu
# 
# ======================================================================
# 5. ALGORITMA SHORTEST PATH (DIJKSTRA)
# ======================================================================
# 
# Skenario: Jalur optimal penyampaian informasi dari Alice ke Henry
# 
# Jalur Optimal: Alice → Henry
# Rute: Alice → Eve → Henry
# 
# Detail Perhitungan:
#   Alice → Eve: 12 pesan/minggu, waktu relatif = 0.0833
#   Eve → Henry: 15 pesan/minggu, waktu relatif = 0.0667
# 
# Akumulasi waktu relatif total: 0.1500
# 
# ======================================================================
# 6. ANALISIS CENTRALITY
# ======================================================================
# 
# --- a) Degree Centrality ---
# Alice  : 0.4286
# Bob    : 0.4286
# Carol  : 0.5714
# David  : 0.5714
# Eve    : 0.7143 (Nilai Tertinggi)
# Frank  : 0.4286
# Grace  : 0.5714
# Henry  : 0.2857
# 
# --- b) Eigenvector Centrality ---
# Alice  : 0.3154
# Bob    : 0.3301
# Carol  : 0.4266
# David  : 0.4187
# Eve    : 0.4890 (Nilai Tertinggi)
# Frank  : 0.3413
# Grace  : 0.3837
# Henry  : 0.1951
# 
# Mahasiswa dengan pengaruh tertinggi: Eve
# Interpretasi: Eve memiliki nilai eigenvector centrality tertinggi yang
# mengindikasikan bahwa ia bukan hanya memiliki banyak koneksi, tetapi juga
# terhubung dengan individu-individu yang memiliki pengaruh signifikan.
# 
# --- c) Closeness Centrality ---
# Alice  : 0.4667
# Bob    : 0.4667
# Carol  : 0.5385
# David  : 0.5385
# Eve    : 0.6364 (Nilai Tertinggi)
# Frank  : 0.4667
# Grace  : 0.5385
# Henry  : 0.3889
# 
# ======================================================================
# 7. DETEKSI KOMUNITAS (SPECTRAL CLUSTERING)
# ======================================================================
# 
# --- Matriks Laplacian: L = D - A ---
# 
# --- Nilai Eigenvalue dari Laplacian ---
# λ1 = 0.000000 (selalu bernilai 0 untuk graf yang terhubung)
# λ2 = 0.585786 (Algebraic Connectivity)
# λ3 = 2.000000
# λ4 = 3.000000
# λ5 = 4.000000
# λ6 = 4.000000
# λ7 = 5.414214
# λ8 = 6.000000
# 
# Algebraic Connectivity (λ₂): 0.5858
# 1. Mengukur tingkat konektivitas dari graf
# 2. Nilai lebih dari 0 menandakan graf terhubung
# 3. Nilai yang lebih besar mengindikasikan konektivitas yang lebih kuat
# 
# --- Fiedler Vector (untuk Proses Clustering) ---
# Alice  :   0.4159
# Bob    :   0.3824
# Carol  :   0.1912
# David  :   0.0000
# Eve    :  -0.3824
# Frank  :  -0.1912
# Grace  :  -0.4159
# Henry  :  -0.5000
# 
# --- Hasil Deteksi Komunitas (2 kelompok) ---
# Kelompok 1: Eve, Frank, Grace, Henry
# Kelompok 2: Alice, Bob, Carol, David
# 
# Interpretasi:
# 1. Kelompok 1: Terdiri dari mahasiswa dengan nilai Fiedler negatif
# 2. Kelompok 2: Terdiri dari mahasiswa dengan nilai Fiedler positif
# 3. Pembagian ini menunjukkan keberadaan dua sub-kelompok yang berbeda
#    dalam struktur jaringan sosial
# 
# ======================================================================
# BONUS: DETEKSI KOMUNITAS (GREEDY MODULARITY)
# ======================================================================
# 
# --- Deteksi Komunitas (2 clusters) ---
# Cluster 1: Alice, Bob, Carol, David
# Cluster 2: Eve, Frank, Grace, Henry
# 
# ======================================================================
# ANALISIS SELESAI
# ======================================================================