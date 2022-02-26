# Tugas Kecil 2: Convex Hull

### Tugas Kecil 2 IF2211 Strategi Algoritma

Convex Hull merupakan himpunan titik terkecil yang berisi kumpulan-kumpulan titik yang bersifat convex. Himpunan titik dikatakan convex apabila untuk sembarang dua buah titik yang berada pada himpunan tersebut, seluruh segmen garis yang berakhir pada dua titik tersebut berada pada himpunan tersebut. Berikut ini adalah ilustrasi mengenai poligon yang convex dan tidak.

Pada repository ini berisi implementasi library convex hull untuk mencari convex hull yang ada pada suatu kumpulan titik.

## Prasyarat

Untuk menggunakan pustaka pada repository ini, diperlukan prasyarat sistem sebagai berikut:

- Python versi 3.9.2
- Library numpy versi 1.22.2

Untuk melihat visualisasi data, diperlukan prasayat sebagai berikut

- Library IPython
- Library Matplotlib
- Library Jupyter Notebook/Jupyterlab
- Library pandas
- Library sklearn (opsional)

Untuk melakukan pengujian unit test, anda perlu menginstall:

- Library pytest

Semua pustaka diatas dapat diinstall secara langsung menggunakan perintah berikut

```shell
pip install - r requirements.txt
```

## Cara Menjalankan Program

Berikut ini adalah langkah untuk menjalankan program:

1. Jika anda ingin melakukan hasil convex hull dari sebuah kumpulan titik, anda perlu menjalankan jupyter lab. Untuk itu jalankan perintah berikut:

```shell
jupyter lab src
```

2. Setelah muncul antarmuka jupyter lab, pilihlah file `notebook.ipynb`.
3. Pilihlah kernel yang diinginkan. Anda dapat memilih pada pojok kanan atas.
4. Untuk menjalankan semua cell, klik `Run` pada bagian atas lalu klik `Run All Cells`.
5. Semua cell akan tereksekusi.

Untuk melakukan unit testing, anda dapat menjalankan perintah berikut:

```
pytest src
```

## Identitas Pembuat

Library ini dibuat oleh Bayu Samudra (13520128)
