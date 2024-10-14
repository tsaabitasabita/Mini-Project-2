# Mini-Project-2

**Nama   :Tsabitah Kawiwara**

**NIM    :2409116099**

**Kelas  :Sistem Informasi C**


# Flowchart Sistem Rekomendasi Buku
![fc 1](https://github.com/user-attachments/assets/b25b3ab1-174b-4f9f-91fd-8298bb8407a3)
![fc2](https://github.com/user-attachments/assets/9a4eb1c1-cdbc-471e-aa92-1a11b926c06a)

![fc3](https://github.com/user-attachments/assets/ebf3d24e-a7ac-405e-ab1d-7179c1dcc16c)

![fc4](https://github.com/user-attachments/assets/d304878c-492d-4064-964c-28f219cbd39c)

![fc5](https://github.com/user-attachments/assets/108c12ee-ccbb-4cb8-b79d-04fbd6248571)

# Penjelasan cara kerja sistem

![gambar 1](https://github.com/user-attachments/assets/b87c1607-5753-4d78-a113-19584e38c497)

Pada gambar diatas, adalah pembukaan program yang akan meminta user untuk menginput/memasukkan pilihan menu dengan angka yang sesuai pada tabel yang ditampilkan. Jika memiloih 1, maka program akan langsung meminta user untuk mengisi username dan passsword untuk ke menu admin berikutnya. Jika memilih 2, maka program akan menampilkan 2 pilihan menu klien. Jika memilih 3, maka program akan selesai.

![gambar 2](https://github.com/user-attachments/assets/f47b3a2e-f2ed-43e7-bcde-d79d00bf3c2b)

Ini adalah tampilan ketika user meimilih 1, dimana user akan diminta mengisi username dan password sebelum masuk ke menu admin


Ketika username dan password telah sesuai, maka login berhasil dan program akan menampilkan menu admin yang terdiri dari 5 pilihan. 
1. Pilihan 1 = admin dapat menambahkan genre dan koleksi buku
2. pilihan 2 = admin dapat melihat informasi data buku
3. pilihan 3 = admin dapat memperbarui data buku, atau mengubah data buku
4. pilihan 4 = admin dapat menghapus data buku/genre
5. pilihan 5 = admin akan kembali ke menu utama



Gambar diatas adalah tampilan ketikan admin memilih 1, akan ditampilkan tabel data buku dan admin diminta untuk memasukan nama kode/genre/jenis buku yang akan ditambahkan kedalam data. Program akan menambahkan data sesuai dengan yang diminta oleh admin ketika megisi kode/genre/jenis buku.

Hasil data yang telah ditambah

Gambar diatas adalah tampilan ketika admin memilih 2, akan ditampilkan tabel data buku terbaru jika sebelumnya admin telah menambahkan data, lalu program akan menanyakan "apakah ingin kembali ke menu admin?" jika "ya" maka admin kembali pada menu admin, jika "tidak" maka program tetap menampilkan tabel sesuai pilihan awal admin.



Gambar diatas adalah tampilan ketika admin memilih 3, akan ditampilan tabel data buku dan admin diminta untuk mengisi kode manakah yang ingin perbarui. Setelah itu program akan menanyakan apakah ingin memperbarui genre?, pada bagian ini karena berupa pertanyaan (decision) maka admin dapat mengisi "tidak" jika tidak ingin memperbarui genre dan program akan tetap berlanjut. Jika admin mengisi "ya" maka program akan meminta admin untuk mengisi genre baru. Selanjutnya program akan menanyakan lagi apakah ingin memperbarui buku?, jika "ya" maka program meminta mengisi jenis buku baru, dan jika "tdiak" maka progran akan memperbarui data dan menampilkan tabel terbaru setelah data diperbarui.


Hasil data yang telah diperbarui




Gambar diatas adalah tampilan ketika admin memilih 4, akan ditampilkan tabel data buku dan admin diminta untuk mengisi kode dan bagian mana yang ingin dihapus, program akan menghapus data sesuai dengan yang diisi admin.


Hasil data buku setelah salah satu data nya telah di hapus


Ketika admin memilih 5, maka akan kembali ke menu utama.

Gambar diatas adalah tampilan ketika user memilih 2 pada menu utama.
Program akan menampilkan menu klien, dan meminta klien untuk memilih menu sesuai dengan tujuan klien. Ketika klien memilih 1, maka program meminta untuk mengisi username dan password. Jika username dan password benar makan program melanjutkan ke menu klien berikutnya.


Ketika klien memilih 1, program akan menampilkan daftar genre berupa tabel, dan meminta klie untuk mengisi nomor genre yang klien minati. Setelah itu program langsung menampilkan beberapa judul buku yang sesuai dengan genre yang klien pilih. Program juga menanyakan apakah ingin memilih genre lagi?, jika "ya" maka program meminta mengisi pilihan genre jika "tidak" akan kembali ke menu klien.


Kembali lagi pada menu utama, ketika user memilih 3, makan program selesai dan tidak melanjutkan proses 
