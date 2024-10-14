# Mini-Project-2

**Nama   :Tsabitah Kawiswara**

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

Pada gambar diatas, adalah pembukaan program yang akan meminta user untuk menginput/memasukkan pilihan menu dengan angka yang sesuai pada tabel yang ditampilkan. Jika memilih 1, maka program akan langsung meminta user untuk mengisi username dan passsword untuk ke menu admin berikutnya. Jika memilih 2, maka program akan menampilkan 2 pilihan menu klien. Jika memilih 3, maka program akan selesai.

![gambar 2](https://github.com/user-attachments/assets/f47b3a2e-f2ed-43e7-bcde-d79d00bf3c2b)

Gambar diatas adalah tampilan ketika user meimilih 1(login), dimana user akan diminta mengisi username dan password sebelum masuk ke menu admin(menjadi admin)

![gammbar 3](https://github.com/user-attachments/assets/ddb32901-2190-432a-9717-e6e814fd664f)

Ketika username dan password telah sesuai, maka login berhasil dan program akan menampilkan menu admin yang terdiri dari 5 pilihan. 
1. Pilihan 1 = admin dapat menambahkan genre dan koleksi buku
2. pilihan 2 = admin dapat melihat informasi data buku
3. pilihan 3 = admin dapat memperbarui data buku, atau mengubah data buku
4. pilihan 4 = admin dapat menghapus data buku/genre
5. pilihan 5 = admin akan kembali ke menu utama

![gambar 4](https://github.com/user-attachments/assets/4155557d-d215-43b1-8f42-b1d4f10e1f93)

Gambar diatas adalah tampilan ketikan admin memilih 1(create), akan ditampilkan tabel data buku dan admin diminta untuk memasukan nama kode/genre/jenis buku yang akan ditambahkan kedalam data. Program akan menambahkan data sesuai dengan yang diminta oleh admin ketika megisi kode/genre/jenis buku.

Hasil data yang telah ditambah pada gambar dibawah ini
![tambah](https://github.com/user-attachments/assets/7d490c6c-bc43-4aff-b6d8-b24cba6dfb23)

![gambar 5](https://github.com/user-attachments/assets/32be90bb-6dac-4654-b188-b36df0384b5a)

Gambar diatas adalah tampilan ketika admin memilih 2(read), akan ditampilkan tabel data buku terbaru jika sebelumnya admin telah menambahkan data, lalu program akan menanyakan "apakah ingin kembali ke menu admin?" jika "ya" maka admin kembali pada menu admin, jika "tidak" maka program tetap menampilkan tabel sesuai pilihan awal admin.

![gambar 6](https://github.com/user-attachments/assets/6701a22f-ffc1-4bbb-b3de-ca5862544e95)

Gambar diatas adalah tampilan ketika admin memilih 3(update), akan ditampilan tabel data buku dan admin diminta untuk mengisi kode manakah yang ingin perbarui. Setelah itu program akan menanyakan apakah ingin memperbarui genre?, pada bagian ini karena berupa pertanyaan (decision) maka admin dapat mengisi "tidak" jika tidak ingin memperbarui genre dan program akan tetap berlanjut. Jika admin mengisi "ya" maka program akan meminta admin untuk mengisi genre baru. Selanjutnya program akan menanyakan lagi apakah ingin memperbarui buku?, jika "ya" maka program meminta mengisi jenis buku baru, dan jika "tdiak" maka progran akan memperbarui data dan menampilkan tabel terbaru setelah data diperbarui.

Hasil data yang telah diperbarui pada gambar dibawah ini
![baru](https://github.com/user-attachments/assets/1c9a5890-8df7-44ae-bcc2-6396fdcae7d9)

![gambar7](https://github.com/user-attachments/assets/84fa6900-998c-4f83-8751-8a9fe3a49cea)

Gambar diatas adalah tampilan ketika admin memilih 4(delete), akan ditampilkan tabel data buku dan admin diminta untuk mengisi kode dan bagian mana yang ingin dihapus, program akan menghapus data sesuai dengan yang diisi admin.


Hasil data buku setelah salah satu data nya telah di hapus pada gambar dibawah ini
![gambar 8](https://github.com/user-attachments/assets/9afdb026-4c64-43ed-8552-cee279d47cdf)



![gambar 9](https://github.com/user-attachments/assets/ed2b629a-5e69-40ab-9daa-ee4002331cda)

Gambar diatas adalah tampilan ketika user memilih 2 pada menu utama (menjadi klien)
Program akan menampilkan menu klien, dan meminta klien untuk memilih menu sesuai dengan tujuan klien. Ketika klien memilih 1(login), maka program meminta untuk mengisi username dan password. Jika username dan password benar makan program melanjutkan ke menu klien berikutnya.

![gambar 10](https://github.com/user-attachments/assets/83cc8622-3ecf-4479-9f88-6de94429deb4)

Ketika klien memilih 1(rekoemndasi buku) pada menu klien setelah login, program akan menampilkan daftar genre berupa tabel, dan meminta klie untuk mengisi nomor genre yang klien minati. Setelah itu program langsung menampilkan beberapa judul buku yang sesuai dengan genre yang klien pilih. Program juga menanyakan apakah ingin memilih genre lagi?, jika "ya" maka program meminta mengisi pilihan genre jika "tidak" akan kembali ke menu klien.

![gambar 11](https://github.com/user-attachments/assets/41aed9de-526a-422f-a0cd-4b35654f58d4)

Kembali lagi pada menu utama, ketika user memilih 3(berhenti), makan program selesai dan tidak melanjutkan proses seperti pada gambar diatas 
