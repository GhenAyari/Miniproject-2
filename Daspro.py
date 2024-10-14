from prettytable import PrettyTable



#daftar mobil yang tersedia sama tarif per hari
mobil_tersedia = {
    'Toyota Avanza': 600000,
    'Honda Jazz': 500000,
    'Daihatsu Xenia': 450000,
    'Mitsubishi Xpander': 650000,
    'Innova barong diesel': 550000,
    'Honda BRV 2022': 730000 
}

register_customer = {}
rental_data = {}


#fungsi untuk nampilkan tabel pilihan
def nampilkan_menu():
    table = PrettyTable()
    table.field_names = ["Pilihan", "Keterangan"]
    table.add_row(["1.", "Pegawai"])
    table.add_row(["2.", "Customer"])
    table.add_row(["3.", "Keluar"]) 
    print(table)

#fungsi untuk validasi login Pegawai
def login_pegawai():
    nama = input("Masukkan Nama: ")
    password = input("Masukkan Password: ")

    #validasi nama dan password
    if nama == "Ghen" and password == "1610":
        print("Login berhasil!\nKerja Ghen jangan malas terus.")
        return True
    else:
        print("Duh kok bisanya lupa")
        return False

#fungsi buat registrasi customer
def register_customer_fungsi():
    print("Registrasi Customer:")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    nik = input("Masukkan NIK KTP: ")

    # Menyimpan data registrasi ke dalam dictionary
    register_customer[nama] = {
        'nama': nama,
        'alamat': alamat,
        'nik': nik
    }
    print("\nRegistrasi berhasil!, sekarang login pakai data yang sama.\n")

    return nama, alamat, nik

#fungsi buat login customer
def login_customer(nama_terdaftar, alamat_terdaftar, nik_terdaftar):
    print("Login Customer:")
    nama = input("Masukkan Nama: ")
    alamat = input("Masukkan Alamat: ")
    nik = input("Masukkan NIK KTP: ")

    if nama == nama_terdaftar and alamat == alamat_terdaftar and nik == nik_terdaftar:
        print("Login berhasil!")
        return True
    else:
        print("Duh salah\n")
        return False

#fungsi buat nampilkan daftar mobil dan tarifnya
def tampilkan_mobil():
    table = PrettyTable()
    table.field_names = ["No", "Nama Mobil", "Tarif per Hari (Rp)"]
    for i, (mobil, tarif) in enumerate(mobil_tersedia.items(), start=1):
        table.add_row([i, mobil, tarif])
    print(table)

#fungsi untuk proses penyewaan mobil oleh customer
def sewa_mobil(nama_customer):
    print("\nDaftar Mobil yang Tersedia dan Tarifnya:")
    tampilkan_mobil()

    #minta input mobil dari customer
    pilihan_mobil = int(input("Pilih mobil yang ingin disewa (masukkan nomor): "))
    if 1 <= pilihan_mobil <= len(mobil_tersedia):
        mobil_pilihan = list(mobil_tersedia.keys())[pilihan_mobil - 1]  
        lama_sewa = int(input(f"Berapa hari Anda ingin menyewa {mobil_pilihan}? "))
        biaya_total = mobil_tersedia[mobil_pilihan] * lama_sewa

        #nyimpan data penyewaan
        rental_data[nama_customer] = {
            'mobil': mobil_pilihan,
            'lama': lama_sewa,
            'biaya_total': biaya_total
        }
        
        #hapus mobil dari daftar mobil yang tersedia
        del mobil_tersedia[mobil_pilihan]
        
        print(f"Anda telah memilih {mobil_pilihan} untuk {lama_sewa} hari. Total biaya: Rp{biaya_total}")
    else:
        print("Mobil tidak tersedia. Kembali ke menu.")

#fungsi untuk mengembalikan mobil yang disewa oleh customer
def kembalikan_mobil(nama_customer):
    if nama_customer in rental_data:
        mobil_dikembalikan = rental_data[nama_customer]['mobil']
        
        #ngembalikan mobil ke daftar mobil yang tersedia
        mobil_tersedia[mobil_dikembalikan] = rental_data[nama_customer]['biaya_total'] // rental_data[nama_customer]['lama']
        
        #menghapus data rental
        print(f"Mobil {mobil_dikembalikan} telah dikembalikan.")
        del rental_data[nama_customer]
        print("Pengembalian berhasil. Mobil telah kembali tersedia.")
    else:
        print("Anda belum menyewa mobil. Kembali ke menu utama.")

#fungsi untuk proses customer
def customer_menu():
    while True:
        #tabel untuk pilihan customer
        table = PrettyTable()
        table.field_names = ["Pilihan", "Keterangan"]
        table.add_row(["1.", "Ingin Melakukan Rental"])
        table.add_row(["2.", "Mengembalikan Mobil"])
        table.add_row(["3.", "Tidak Melakukan Rental"])
        print(table)

        pilihan = int(input("Apa yang ingin Anda lakukan? "))

        if pilihan == 1:
            #proses registrasi customer
            nama_terdaftar, alamat_terdaftar, nik_terdaftar = register_customer_fungsi()

            #habis registrasi, customer harus login kembali
            if login_customer(nama_terdaftar, alamat_terdaftar, nik_terdaftar):
                print("Proses rental dapat dilanjutkan.\n")
                
                #nampilkan pilihan untuk rental mobil
                table = PrettyTable()
                table.field_names = ["Pilihan", "Keterangan"]
                table.add_row(["1.", "Lihat Daftar Mobil dan Tarif"])
                print(table)

                opsi = int(input("Masukkan pilihan: "))
                if opsi == 1:
                    sewa_mobil(nama_terdaftar)
                else:
                    print("Pilihan tidak valid.")
                break
            else:
                break 
        elif pilihan == 2:
            print("Anda memilih untuk mengembalikan mobil.")
            nama = input("Masukkan nama anda untuk pengembalian: ")
            kembalikan_mobil(nama)  #manngil fungsi untuk mengembalikan mobil
        elif pilihan == 3:
            print("Anda memilih untuk tidak melakukan rental. Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#fungsi untuk menampilkan penyewa mobil
def lihat_penyewa():
    if rental_data:
        table = PrettyTable()
        table.field_names = ["Nama", "Mobil", "Lama Sewa (Hari)", "Total Biaya (Rp)"]
        for nama, data in rental_data.items():
            table.add_row([nama, data['mobil'], data['lama'], data['biaya_total']])
        print(table)
    else:
        print("Belum ada yang menyewa mobil.")

#fungsi untuk menambahkan mobil baru
def tambah_mobil():
    mobil_baru = input("Masukkan nama mobil yang ingin ditambahkan: ")
    tarif_baru = int(input("Masukkan tarif per hari (Rp): "))
    mobil_tersedia[mobil_baru] = tarif_baru
    print(f"Mobil {mobil_baru} dengan tarif Rp{tarif_baru} berhasil ditambahkan.")
    tampilkan_mobil()

#fungsi untuk menghapus mobil yang tersedia
def hapus_mobil():
    tampilkan_mobil()
    mobil_hapus = int(input("Masukkan nomor mobil yang ingin dihapus: "))
    if 1 <= mobil_hapus <= len(mobil_tersedia):
        mobil_pilihan = list(mobil_tersedia.keys())[mobil_hapus - 1]
        del mobil_tersedia[mobil_pilihan]
        print(f"Mobil {mobil_pilihan} berhasil dihapus.")
        tampilkan_mobil()
    else:
        print("Pilihan tidak valid.")

#fungsi untuk proses pegawai
def pegawai_menu():
    while True:
        table = PrettyTable()
        table.field_names = ["Pilihan", "Keterangan"]
        table.add_row(["1.", "Lihat Penyewa"])
        table.add_row(["2.", "Menambahkan Mobil"])
        table.add_row(["3.", "Hapus Mobil"])
        table.add_row(["4.", "Keluar"])
        print(table)

        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            lihat_penyewa()
        elif pilihan == 2:
            tambah_mobil()
        elif pilihan == 3:
            hapus_mobil()
        elif pilihan == 4:
            print("Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid.")

#fungsi utama
def main():
    while True:
        print("Selamat Datang Di Penyewaan Mobil G16\n") 
        nampilkan_menu() 
        
        pilihan = int(input("Jadi kamu sebagai apa? "))

        if pilihan == 1:
            if login_pegawai():  
                pegawai_menu()
        elif pilihan == 2:
            customer_menu()
        elif pilihan == 3:
            print(50*"=")
            print(50*"=")
            print("                    Makasih ya.")
            print(50*"=")
            print(50*"=")
            exit()
        else:
            print("Pilihan ga valid. coba lagi!")


main()
