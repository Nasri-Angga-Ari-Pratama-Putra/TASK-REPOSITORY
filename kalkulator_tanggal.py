def validasi_input():
    while True:
        try:
            tanggal = int(input("Masukkan Tanggal (1-31): "))
            if tanggal < 1 or tanggal > 31:
                print("Tanggal harus diisi antara 1 s.d 31, ulangi!")
                continue
            bulan = int(input("Masukkan bulan (1-12): "))
            if bulan < 1 or bulan > 12:
                print("bulan harus diisi antar 1 s.d 12, ulangi!")
                continue
            tahun = int(input("masukkan tahun: "))
            if tahun <1:
                print("Tahun harus angka positif, Ulangi!")
                continue
            return(tanggal, bulan, tahun)
        except ValueError:
            print("Harus Masukkan angka bro, ulangi!!")

tanggal, bulan, tahun = validasi_input()

# cek tahun kabisat untuk rentang tahun
print("\nCek Tahun Kabisat Untuk Rentang Tahun:")
for tahun in range(tahun-2,tahun+3):
    if tahun % 4 == 0 and (tahun % 100 != 0) or (tahun % 400 == 0):
        print(f"Tahun {tahun} adalah Tahun Kabisat")

    else:
        print(f"Tahun {tahun} bukan Tahun Kabisat")

# Zeller's Congruence untuk hitung hari
if bulan == 1 or bulan == 2:
    bulan += 12
    tahun -= 1

K = tahun % 100
J = tahun // 100

h = (tanggal + ((13 * (bulan + 1)) // 5) + K + (K // 4)+(J // 4) - 2 * J) % 7
print("\nHasil Perhitungan Hari Adalah:")
if h == 0:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Sabtu")

elif h == 1:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Minggu")

elif h == 2:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Senin")

elif h == 3:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Selasa")

elif h == 4:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Rabu")

elif h == 5:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Kamis")

else:
    print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari Jum'at")


