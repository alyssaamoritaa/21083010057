#import library
from os import getpid
from time import time, sleep
from multiprocessing import Pool, Process

#inisialisasi fungsi yang akan digunakan
def cetak(i):
    if (i+1)%2 == 0:
       print(i+1, "Genap - ID proses", getpid())
       sleep(1)
    else:
       print(i+1, "Ganjil - ID proses", getpid())
       sleep(1)

#input bilangan
a = int(input("Masukkan Angka : "))

#sekuensial
print("\nSekuensial")
#untuk mendapatkan waktu sebelum eksekusi
sekuensial_awal = time()

#proses berlangsung
for i in range(a):
    cetak(i)

#untuk mendapatkan waktu setelah eksekusi
sekuensial_akhir = time()

#multiprocessing dengan kelas process
print("\nmultiprocessing.Process")
#untuk menampung proses-proses
kumpulan_process = []

#untuk mendapatkan waktu sebelum eksekusi
process_awal = time()

#proses berlangsung
for i in range(a):
    p = Process(target=cetak, args=(i,))
    kumpulan_process.append(p)
    p.start()

#untuk menggabungkan proses-proses agar tidak loncat ke proses sebelumnya
for i in  kumpulan_process:
    p.join()

#untuk mendapatkan waktu setelah eksekusi
process_akhir = time()

#multiprocessing dengan kelas pool
print("\nmultiprocessing.Pool")
#untuk mendapatkan waktu sebelum eksekusi
pool_awal = time()

#proses berlangsung
pool = Pool()
pool.map(cetak, range(0,a))
pool.close

#untuk mendapatkan waktu sebelum eksekusi
pool_akhir = time()

#bandingkan waktu eksekusi
print("\nWaktu eksekusi sekuensial : ", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process : ", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool : ", pool_akhir - pool_awal, "detik")
