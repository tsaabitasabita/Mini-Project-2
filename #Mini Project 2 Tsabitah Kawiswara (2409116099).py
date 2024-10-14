#Mini Project 2 Tsabitah Kawiswara (2409116099)

from prettytable import PrettyTable

# Data
data = {
    "kode": ["01", "02", "03", "04", "05"],
    "genre": ["romance", "fantasy", "comedy", "horror", "mystery"],
    "buku": [
        "Butterflies, Serangkai, Check and Mate",
        "Harry Potter, Red Queen, Strange the Dreamer",
        "Ngenest, Ubur-ubur Lembur",
        "Kisah Tanah Jawa, Another, Holy Mother",
        "Pengacara Penipu, The Borrowed, The Da Vinci Code"
    ]
}
# Login Admin
def login_admin():
    print("------------------------------------------------------")
    print("                     LOGIN ADMIN                      ")
    print("------------------------------------------------------")
    while True:
        try:
            nama = input("Username: ")
            password = input("Password: ")
            if nama == "bita" and password == "99":
                print("LOGIN BERHASIL")
                print("ANDA MASUK SEBAGAI ADMIN!")
                menu_admin()  
            else:
                print("LOGIN GAGAL, SILAHKAN COBA LAGI")
        except ValueError:
            print("perhatikan pengisian data")
            kembali = input("Apakah anda ingin kembali ke menu utama? (ya/tidak): ")
        if kembali == "ya":
            mulai_program()  
            break
        elif kembali == "tidak":
            continue  
        else:
            print("MAAF, PILIHAN TIDAK TERSEDIA")

# Login Klien
def login_klien():
    print("------------------------------------------------------")
    print("                    LOGIN KLIEN                       ")
    print("------------------------------------------------------")
    while True:
            nama = input("Masukkan Username Anda: ")
            password = input("Masukkan Password Anda: ")
            if nama == "bita" and password == "99":
                print("----------LOGIN BERHASIL----------")
                menu_klien2()  
                break  
            else:
                print("LOGIN GAGAL, SILAHKAN COBA LAGI")
            kembali = input("Apakah anda ingin kembali ke menu utama? (ya/tidak): ")
            if kembali == "ya":
                mulai_program()  
                break  
            elif kembali == "tidak":
                continue  
            else:
                print("MAAF, PILIHAN TIDAK TERSEDIA")
        
        



#Create (Admin)
from prettytable import PrettyTable

# Inisialisasi data awal
data = {
    "kode": ["01", "02", "03", "04", "05"],
    "genre": ["romance", "fantasy", "comedy", "horror", "mystery"],
    "buku": [
        "Butterflies, Serangkai, Check and Mate",
        "Harry Potter, Red Queen, Strange The Dreamer",
        "Ngenest, Ubur-ubur Lembur, Kambing Jantan",
        "Kisah Tanah Jawa, Another, Holy Mother",
        "Pengacara Penipu, The Borrowed, The Da Vinci Code"
    ]
}

def create():
    print("-------------MENAMBAHKAN KOLEKSI BUKU------------")
    read()  
    while True:
        try:
            print("Masukkan data yang ingin ditambah")
            kode = input("Kode: ")
            genre = input("Genre: ")
            buku = input("Buku: ")

            if kode in data["kode"]:
                print("Kode sudah ada. Silakan gunakan kode yang berbeda.")
                continue
            
            data["kode"].append(kode)
            data["genre"].append(genre)
            data["buku"].append(buku)

            print("----------------DATA BERHASIL DITAMBAHKAN--------------")
            read()  
            break
        except ValueError:
            print("Masukan data yang sesuai!")

#read (Admin)
def read():
    table = PrettyTable()
    table.field_names = ["No", "Kode", "Genre", "Buku"]

    rows = []  
    for i in range(len(data["kode"])):
        nomor = i + 1
        kode = data["kode"][i]
        genre = data["genre"][i]
        buku = data["buku"][i]

        rows.append((nomor, kode, genre, buku))

    for row in rows:
        table.add_row(row)

    print(table)


#Update (Admin)
def update():
    print("----------------MEMPERBARUI DATA BUKU--------------------")
    read()
    while True:
        try:
            kodeedit = input("Masukkan kode yang ingin diperbarui: ")
            cari_n = -1
            for i in range(len(data["kode"])):
                if data["kode"][i] == kodeedit:
                    cari_n = i 
                    break
            if cari_n == -1:
                print("Masukkan data yang sesuai")
                continue
            break
        except ValueError:
            print("Masukkan data yang sesuai")

    while True:
        newgenre = input("\nApakah anda ingin memperbarui genre? (ya/tidak): ")
        if newgenre == "ya":
            genre_baru = input("Masukan genre baru: ")
            if genre_baru in data["genre"]:
                print("\nGENRE SUDAH ADA")
            else:
                data["genre"][cari_n] = genre_baru
                print("\n          --- GENRE BERHASIL DIPERBARUI ---\n")
                break
            
        elif newgenre == "tidak":
            break
        else:
            print("\nPILIHAN TIDAK TERSEDIA")

    while True:
        newbook = input("\nApakah anda ingin memperbarui buku? (ya/tidak): ")
        if newbook == "ya":
            while True:
                new_book = input("Masukkan buku baru: ")
                data["buku"][cari_n] = new_book
                print("\n         --- DATA BERHASIL DIPERBARUI ---        \n")
                break
        elif newbook == "tidak":
            break
        else:
            print("\nPILIHAN TIDAK TERSEDIA")
        read()

#Delete (Admin)2
def delete():
    read() 
    print("\n         --- MENGHAPUS DATA BUKU---        \n")
    while True:
        hapus_g = input("Masukkan kode buku yang akan dihapus: ")
        
        if hapus_g == "":
            print("\nINPUT TIDAK BOLEH KOSONG")
            continue
        
        if hapus_g in data["kode"]:
            cari_n = data["kode"].index(hapus_g)
            print("Anda ingin menghapus:")
            print(f"1. Kode: {data['kode'][cari_n]}")
            print(f"2. Genre: {data['genre'][cari_n]}")
            print(f"3. Buku: {data['buku'][cari_n]}")
            pilihan = input("Pilih bagian yang ingin dihapus (1/2/3): ")
            
            if pilihan == "1":
                del data["kode"][cari_n]
                print("\n      --- KODE BERHASIL DIHAPUS ---\n")
            elif pilihan == "2":
                del data["genre"][cari_n]
                print("\n      --- GENRE BERHASIL DIHAPUS ---\n")
            elif pilihan == "3":
                del data["buku"][cari_n]
                print("\n      --- BUKU BERHASIL DIHAPUS ---\n")
            else:
                print("\nPILIHAN TIDAK VALID")
                continue
            read()  
            break
        else:
            print("\n       --- KODE TIDAK DITEMUKAN ----\n")


#Rekomendasi Buku (Klien)
def rekomendasi_buku():
    while True:
        table = PrettyTable()
        table.title = "GENRE BUKU"
        table.field_names = ["No", "Genre"]
        table.add_rows([
            [1, "Romance     "],
            [2, "Fantasy     "],
            [3, "Comedy      "],
            [4, "Horror      "],
            [5, "Mystery     "]
        ])
        print(table)

        try:
            genre = int(input("Masukkan nomor genre buku yang anda minati: "))
            
            if genre == 1:
                print("Ini adalah rekomendasi buku yang mungkin anda sukai!")
                print("Butterflies, Serangkai, Check and Mate")
            elif genre == 2:
                print("Ini adalah rekomendasi buku yang mungkin anda sukai!")
                print("Harry Potter, Red Queen, Strange The Dreamer")
            elif genre == 3:
                print("Ini adalah rekomendasi buku yang mungkin anda sukai!")
                print("Ngenest, Ubur-ubur Lembur, Kambing Jantan")
            elif genre == 4:
                print("Ini adalah rekomendasi buku yang mungkin anda sukai!")
                print("Kisah Tanah Jawa, Another, Holy Mother")
            elif genre == 5:
                print("Ini adalah rekomendasi buku yang mungkin anda sukai!")
                print("Pengacara Penipu, The Borrowed, The Da Vinci Code")
            else:
                print("Pilihan genre tidak valid.")
                continue
            
        except ValueError:
            print("Input tidak valid. Silakan masukkan nomor genre.")
            continue

        rekomendasi_lanjut = input("Apakah ingin memilih genre lagi? (ya/tidak): ")
        if rekomendasi_lanjut != "ya":
            break



        
#Menu admin
def menu_admin():
    table = PrettyTable()
    table.title = "Menu Admin"
    table.field_names = ["No" , "Aktivitas"]
    table.add_rows([
        [1, "Tambah koleksi buku   "],
        [2, "Lihat Informasi buku  "],
        [3, "Perbarui stok buku    "],
        [4, "Hapus genre buku      "],
        [5, "Kembali               "]
    ])
    print(table)

    while True:
            menu = int(input("Masukan pilihan menu : "))
            if menu == 1:
                
                while True:
                    create()
                    Lanjut = input("Apakah anda ingin menambahkan data lagi? (ya/tidak) : ")
                    if Lanjut == "ya":
                        create()
                    elif Lanjut == "tidak":
                        menu_admin()
                    else :
                        print("\nINPUT TIDAK VALID")
                    
            elif menu == 2:
                
                while True :
                    read()
                    Lanjut = input("Apakah anda ingin kembali ke menu admin? (ya/tidak) : ")
                    if Lanjut == "ya":
                        menu_admin()
                        
                    elif Lanjut == "tidak":

                        print("\n        --- MENAMPILKAN DATA ---   \n")

                    else :
                        print("\nINPUT TIDAK VALID")

            elif menu == 3:
                
                while True:
                    update()
                    Lanjut = input("Apakah anda ingin mengubah data lagi? (ya/tidak) : ")
                    if Lanjut == "ya":
                        print("\nSILAKAN UPDATE DATA LAGI")
                    elif Lanjut == "tidak":
                        menu_admin()
                        
                        break
                    else :
                        print("\nINPUT TIDAK VALID")

            elif menu == 4:
        
                while True:
                    delete()
                    Lanjut = input(">> Apakah anda ingin menghapus data lagi? (ya/tidak) : ")
                    if Lanjut == "ya":
                        print("\n SILAKAN HAPUS DATA LAGI")
                    elif Lanjut == "tidak":
                        menu_admin()
                        break
                    else :
                        print("\nINPUT TIDAK VALID")
                        
            elif menu == 5:  
                mulai_program()
            else:
                print("\nPILIHAN TIDAK TERSEDIA")
                print("SILAHKAN COBA LAGI\n")
                menu_admin()
                break
        
        
#Menu Klien 1
def menu_klien1():
    while True :
            table= PrettyTable()
            table.title= "MENU  KLIEN"
            table.field_names= ["No", "Aktivitas"]
            table.add_rows([
                [1, "Login             "    ],
                [2, "Kembali ke menu utama "]
                ])
            print (table)
            menu = int(input("Masukkan pilihan menu : "))
            if menu == 1:
                login_klien()
            else:
                print("\nINPUT TIDAK VALID")
                print("SILAKAN COBA LAGI\n")
                break
                
        

        
#Menu Klien 2
def menu_klien2():
    while True:
            table= PrettyTable()
            table.title= "MENU  KLIEN"
            table.field_names= ["No", "Aktivitas"]
            table.add_rows([
                [1, "Rekomendasi buku  "    ],
                [2, "Kembali ke menu utama "]
                ])
            print (table)
            pilihan = int(input("Masukkan pilihan menu = "))
            if pilihan == 1:
                rekomendasi_buku()
            elif pilihan == 2:
                mulai_program()
            else:
                print("\nPILIHAN TIDAK TERSEDIA")
                print("SILAKAN COBA LAGI")
                break

    
    


#Tampilan Awal  
def mulai_program():
    print("\n             SELAMAT DATANG DI PELAYANAN REKOMENDASI BUKU            ")   
    print("            Merekomendasikan buku sesuai minat bacaan anda           ")
    while True :
        
            table= PrettyTable()
            table.title= "MENU UTAMA"
            table.field_names= ["No", "Role"]
            table.add_rows([
                [1, "Admin  "],
                [2, "Klien  "],
                [3, "Selesai"]
            ])
            print (table)
        
            menu = int(input("Masukan pilihan menu dengan angka : "))
            if menu == 1:
                login_admin()

            elif menu == 2:
                print("------------- SELAMAT DATANG DI MENU KLIEN -------------\n")
                menu_klien1()

            elif menu == 3:
                print("\n---------------- PROGRAM TELAH SELESAI ----------------")
                print("--------------------- TERIMA KASIH --------------------\n")
                break
        
    
        
        
mulai_program()