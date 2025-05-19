import time          # modul 'time' → menyediakan fungsi pengukur waktu
import random        # modul 'random' → untuk membuat data uji acak

# =====================================================================
#  ALGORITMA BRUTE-FORCE  (sesuai pseudocode MinMaks1)
# =====================================================================
def min_maksbf(A):
    """
    Mengembalikan (min_val, maks_val) dari larik A menggunakan
    pendekatan bruteforce satu putaran (O(n)).
    """
    # ---------- DEKLARASI / INISIALISASI -----------------------------
    i = 1                 # variabel penghitung indeks (mulai 1 karena
                          # elemen indeks 0 sudah diasumsikan diproses)
    min_val = A[0]        # asumsikan elemen pertama = nilai minimum awal
    maks_val = A[0]       # asumsikan elemen pertama = nilai maksimum awal

    # ---------- ALGORITMA UTAMA --------------------------------------
    for i in range(1, len(A)):      # iterasi mulai elemen ke-2 s/d terakhir
        if A[i] < min_val:          # cek lebih kecil dari kandidat minimum?
            min_val = A[i]          # → perbarui nilai minimum

        if A[i] > maks_val:         # cek lebih besar dari kandidat maksimum?
            maks_val = A[i]         # → perbarui nilai maksimum

    return min_val, maks_val        # kembalikan sepasang nilai min & max


# =====================================================================
#  ALGORITMA DIVIDE-AND-CONQUER  (sesuai pseudocode MinMaks2)
# =====================================================================
def min_maksdnc(A):
    """Wrapper agar pemanggilan cukup satu argumen (larik A)."""
    #      array  | indeks awal | indeks akhir
    return minmaksdncraw(A, 0, len(A) - 1)


def minmaksdncraw(A, i, j):
    """
    Versi rekursif: memroses larik A dari indeks i hingga j (inklusif)
    dan mengembalikan (nilai_min, nilai_maks).
    """
    # --------- KASUS DASAR 1 : sub-larik berukuran 1 elemen -----------
    if i == j:                       # hanya ada satu elemen di rentang ini
        return A[i], A[i]            # elemen itu otomatis min & maks

    # --------- KASUS DASAR 2 : sub-larik berukuran 2 elemen -----------
    if i == j - 1:                   # dua elemen bersebelahan
        if A[i] < A[j]:              # bandingkan langsung
            return A[i], A[j]        # urutan (min, maks)
        else:
            return A[j], A[i]        # elemen j lebih kecil → tukar

    # --------- KASUS REKURSIF : > 2 elemen ----------------------------
    k = (i + j) // 2                 # cari titik tengah (integer division)
    # Pecah kiri: indeks i .. k
    min1, maks1 = minmaksdncraw(A, i, k)
    # Pecah kanan: indeks k+1 .. j
    min2, maks2 = minmaksdncraw(A, k + 1, j)

    # Gabungkan hasil kedua belahan
    min_final = min1 if min1 < min2 else min2      # ambil yang terkecil
    maks_final = maks2 if maks1 < maks2 else maks1 # ambil yang terbesar
    return min_final, maks_final


print("\nIni hasil dari bruteforce")

data1 = [random.randint(0, 99999999) for _ in range(10)]               # 2) Contoh data (perbanyak agar tes terasa)


start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksbf(data1)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data2 = [random.randint(0, 99999999) for _ in range(20)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksbf(data2)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data3 = [random.randint(0, 99999999) for _ in range(50)]               # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksbf(data3)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data4 = [random.randint(0, 99999999) for _ in range(100)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksbf(data4)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data5 = [random.randint(0, 99999999) for _ in range(200)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksbf(data5)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data6 = [random.randint(0, 99999999) for _ in range(500)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksbf(data6)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)


print("\nIni hasil dari dnc")

data1 = [random.randint(0, 99999999) for _ in range(10)]               # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksdnc(data1)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data2 = [random.randint(0, 99999999) for _ in range(20)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksdnc(data2)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data3 = [random.randint(0, 99999999) for _ in range(50)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksdnc(data3)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data4 = [random.randint(0, 99999999) for _ in range(100)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksdnc(data4)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data5 = [random.randint(0, 99999999) for _ in range(200)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksdnc(data5)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

data5 = [random.randint(0, 99999999) for _ in range(500)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksdnc(data5)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)


print("\ndata besar dnc\n")

databesar = [random.randint(6900, 99999999) for _ in range(1000000)]                # 2) Contoh data (perbanyak agar tes terasa)

start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksdnc(databesar)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)

print("\ndata besar bf \n")


start = time.perf_counter()                   # 3) Mulai stopwatch ‒ paling presisi di Python
min_val, max_val = min_maksbf(databesar)            # 4) Jalankan fungsi yang mau diukur
end = time.perf_counter()                     # 5) Berhenti stopwatch

elapsed = end - start                         # 6) Hitung selisih waktu
print(f"Min: {min_val}, Max: {max_val}")      # 7) Tampilkan hasil fungsi
print(f"Elapsed time: {elapsed:.6f} detik")   # 8) Tampilkan lama eksekusi (6 digit presisi)
