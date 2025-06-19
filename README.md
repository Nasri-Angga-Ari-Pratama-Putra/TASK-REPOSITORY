# TASK-REPOSITORY

### Selamat Datang di Task Repository Saya

---

Pernahkah Anda bertanya-tanya hari apa 17 Agustus 1945? Atau hari apa ulang tahun Anda di tahun 2050 nanti? Zeller's Date Magician hadir untuk menjawabnya! Repository ini berisi implementasi rumus Zeller's Congruence yang elegan untuk secara instan menghitung hari dalam seminggu dari tanggal berapa pun. Selami keajaiban algoritma dan jadikan perhitungan tanggal semudah berkedip! ✨🗓️

### Kegunaan Repository Ini

- Validasi Tanggal dan Hari: Penting untuk memastikan data tanggal Anda akurat. Repository ini dapat membantu Anda memvalidasi apakah hari yang terkait dengan suatu tanggal sudah benar, sangat berguna dalam sistem entri data atau laporan.
- Alat Bantu Pribadi: Butuh tahu hari apa ulang tahun Anda tahun depan, dua tahun sebelum dan sesudah? Atau hari apa hari besar tertentu? Anda bisa menggunakan implementasi ini sebagai alat bantu cepat untuk menjawab pertanyaan-pertanyaan sepele tentang hari dan tanggal.

---

Cara Mendownload 
Ikuti langkah-langkah mudah ini untuk menggunakan aplikasi:

1. Siapkan Python: Pastikan Anda sudah menginstal Python di PC atau laptop Anda. (Saat ini, aplikasi hanya tersedia untuk desktop.)
2. Unduh Aplikasi: Dapatkan file app.py yang dilampirkan di bawah ini.
3. Jalankan dan Masukkan Tanggal: Buka terminal atau command prompt, navigasikan ke lokasi Anda menyimpan app.py, lalu jalankan file tersebut. Anda akan diminta untuk memasukkan tanggal yang Anda inginkan (untuk saat ini hanya mendukung kalender Gregorian).
4. Aplikasi akan langsung memberi tahu Anda hari apa tanggal tersebut.

Download app.py

![image](https://github.com/Nasri-Angga-Ari-Pratama-Putra/TASK-REPOSITORY/blob/main/Download%20app.py.png)

Open cmd

![image](https://github.com/Nasri-Angga-Ari-Pratama-Putra/TASK-REPOSITORY/blob/main/open%20cmd.png)

Run app.py

![image](https://github.com/Nasri-Angga-Ari-Pratama-Putra/TASK-REPOSITORY/blob/main/run%20app.py.png)

Aplikasi Zeller's QuickDate didesain dengan arsitektur modular yang rapi, memastikan validasi input yang kuat dan perhitungan yang akurat. Berikut adalah rincian komponen teknisnya:

1. app.py - Sang Orketrator
Sebagai inti utama aplikasi, app.py berfungsi sebagai orkestrator atau pengendali alur program. Ia bertanggung jawab untuk:

- Menginisiasi interaksi dengan pengguna.
- Memanggil dan mengkoordinasikan fungsi-fungsi dari modul lain (input_validation, leap_year, dan zellers_congruence).
- Menggabungkan hasil dari setiap modul untuk memberikan output akhir kepada pengguna.

2. input_validation Module

Modul ini adalah garda terdepan dalam memastikan integritas data. Tugas utamanya adalah:

- Pengecekan Rentang Parameter: Memastikan input tanggal, bulan, dan tahun yang diberikan pengguna berada dalam rentang yang valid:
-      Tanggal: 1-31
-      Bulan: 1-12
-      Tahun: > 0 (lebih besar dari nol)
- Umpan Balik Interaktif: Jika input yang diberikan pengguna berada di luar rentang yang ditentukan, modul ini akan memberikan umpan balik yang jelas dan meminta pengguna untuk memasukkan kembali nilai yang benar. Proses validasi ini akan terus berulang hingga input yang diberikan memenuhi semua kondisi.

3. leap_year Module

Modul leap_year menangani logika perhitungan tahun kabisat, yang penting untuk akurasi kalender Gregorian, terutama saat berhadapan dengan bulan Februari. Modul ini akan:

- Menghitung Tahun Kabisat: Berdasarkan tahun input, modul ini akan menghitung dan menampilkan apakah tahun tersebut adalah tahun kabisat.
- Rentang Tampilan: Secara spesifik, modul ini akan menghasilkan dan menampilkan daftar tahun kabisat mulai dari 2 tahun sebelum hingga 2 tahun setelah tahun yang dimasukkan pengguna.
- Kriteria Tahun Kabisat: Perhitungan didasarkan pada kriteria standar tahun kabisat Gregorian:
-      Tahun habis dibagi 4 DAN tidak habis dibagi 100, ATAU
-      Tahun habis dibagi 400.
4. zellers_congruence Module

Ini adalah inti perhitungan Zeller's Congruence. Modul ini bertugas untuk:

- Penerapan Algoritma: Mengimplementasikan algoritma Zeller's Congruence untuk kalender Gregorian. Algoritma ini mengambil input tanggal, bulan, dan tahun, lalu melakukan serangkaian perhitungan matematis.
- Pemetaan Hari: Hasil numerik dari algoritma Zeller's Congruence kemudian akan dipetakan ke hari-hari dalam seminggu (contoh: 0 = Sabtu, 1 = Minggu, dst., tergantung implementasi referensi).
- Referensi: Algoritma ini didasarkan pada rumus yang dapat ditemukan di berbagai sumber referensi seperti Wikipedia.

Dengan pembagian tugas yang jelas antar modul ini, aplikasi Anda menjadi mudah dipelihara, diperluas, dan di-debug, sekaligus memastikan fungsionalitas inti berjalan dengan presisi.
