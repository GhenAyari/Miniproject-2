# Miniproject-2
Ghendida Gantari Ayari <br> NIM: 2409116080 <br> Kelas: B 2024

Gambar Flowchart
![daspro](https://github.com/user-attachments/assets/beb153f5-3bb7-4dde-95eb-d5229febcef5)

<br><br>
### Bagian Pegawai
<br><br>
![Screenshot (78)](https://github.com/user-attachments/assets/966fee79-14c3-4c30-ab73-5f0022eea2b0)
Jadi ketika kita memulai program maka akan muncul tiga menu yaitu: 1. Pegawai, 2. Customer, 3. Keluar
<br><br>
<br><br>

![Screenshot (77)](https://github.com/user-attachments/assets/f52881ad-69c1-4670-9253-be302c36a566)
Ketika memilih pilihan ketiga yaitu 3.Keluar maka program akan berhenti
<br><br>
<br><br>

![Screenshot (79)](https://github.com/user-attachments/assets/bd5fc7d4-8d98-4999-a4f8-ca9737f312b9)
Ketika memilih pilihan pertama yaitu sebagai pegawai, harus memasukkan nama dan password yaitu, <br>
Nama: Ghen <br>
Password: 1610 <br>
Jika salah satu salah maka login gagal
<br><br>
<br><br>

![Screenshot (80)](https://github.com/user-attachments/assets/fa2d7df7-4194-43e9-ae11-f1bfe5e02ce6)
Jika memilih pilihan pertama yaitu, 1. Lihat penyewa. Maka akan muncul data penyewanya, <br>
dan juga berapa lama menyewanya, total biaya juga
<br><br>
<br><br>

![Screenshot (81)](https://github.com/user-attachments/assets/dd8d04ed-d7cd-4ec4-9984-613c4a992dcc)
Jika  memilih pilihan kedua yaitu, 2. Menambah mobil, akan muncul innput untuk masukkan nama mobil<br>
dan juga input brp tarifnya perhari
<br><br>
<br><br>

![Screenshot (82)](https://github.com/user-attachments/assets/7067b8bb-ad53-4649-a0f5-1e3b211d8d12)
Jika memilih pilihan ketiga yaitu, 3. Hapus Mobil, lalu pilih mobil mana yang mau dihaous. <br>
contoh: kayak saya menghapus mobil Daihatsu Xenia di nomor 3, dan Daihatsu Xenia terhapus.
<br><br>
<br><br>

![Screenshot (83)](https://github.com/user-attachments/assets/dfdfa935-b300-4ed1-b0da-8adaa68ff2d9)
Jika memilih pilihan 4 yaitu, 4. Keluar maka akan kembali ke menu utama
<br><br>
<br><br>

### Sekarang bagian si customer
<br><br>
![Screenshot (84)](https://github.com/user-attachments/assets/d0ad183d-b358-48dc-a1ec-767c67c5c675)
Di customer ini terdapat tiga pilihan yang pertama pilihan, 1. Ingin melakukan rental jika memilih itu maka,<br>
akan ada input untuk resgistrasi: Nama, Alamat dan NIK (Nomor Induk Kewarnegaraan). Setelah itu customer diminta<br>
memasukkan kembali data yang tadi, pastikan sama seperti yang tadi jika tidak sama maka akan gagal.
<br><br>
<br><br>

![Screenshot (85)](https://github.com/user-attachments/assets/8018cd3a-abe3-4358-ba47-1abedcebcefa)
Setelah selesai registrasi maka akan dilanjutkan dengan memilih mobil dan berapa hari menyewannya.<br>
setelah kita selesai memilih mobil dan berapa lama tarifnya, data tersebut akan masuk di pegawai, dan pegawai<br>
bisa melihat data penyewa serta mobil apa yang dia sewa
<br><br>
<br><br>

![Screenshot (86)](https://github.com/user-attachments/assets/184bb412-6a57-4b1c-9401-f6aa12ee692f)
Udah selesai minjam skrg kembalikan. Kita bisa menngunakan nomor 2 yaitu mengembalikan mobil<br>
dan masukkan nama yang tadi kita gunakan untuk menyewa mobil setelah itu mobil sudah kembali
<br><br>
<br><br>

![Screenshot (87)](https://github.com/user-attachments/assets/d9455925-196e-4610-823d-74e2a2617136)
Ada pilihan nomor 3 yaitu 3. Tidak melakukan rental. dan ketika memilih menu ini maka akan kembali ke menu utama
<br><br>
<br><br>

### Sekarang adalah codenya
<br>
baris pertama:
from prettytable import PrettyTable<br>
Untuk mengimpor library dan membuat tabel yang rapi, menampilkan informasi dalam bentuk tabel
<br>

}<br><br>Baris 5-16:<br><br>
mobil_tersedia = {<br> 
    'Toyota Avanza': 600000,<br>
    'Honda Jazz': 500000,<br>
    'Daihatsu Xenia': 450000,<br>
    'Mitsubishi Xpander': 650000,<br>
    'Innova barong diesel': 550000,<br>
    'Honda BRV 2022': 730000<br>}<br>
register_customer = {}<br>
rental_data = {}<br><br>
mobil_tersedia: Dictionary ini menyimpan daftar mobil yang tersedia untuk disewa, dengan nama mobil sebagai kunci dan tarif sewa per hari (dalam rupiah) sebagai nilai.<br>
register_customer: Dictionary ini akan digunakan untuk menyimpan data customer yang telah melakukan registrasi.<br>
rental_data: Dictionary ini menyimpan informasi penyewaan mobil oleh customer, seperti nama penyewa, mobil yang disewa, lama sewa, dan total biaya.
<br><br>
Baris 20-26:<br><br>
def nampilkan_menu():
    table = PrettyTable()<br>
    table.field_names = ["Pilihan", "Keterangan"]<br>
    table.add_row(["1.", "Pegawai"])<br>
    table.add_row(["2.", "Customer"])<br>
    table.add_row(["3.", "Keluar"])<br>
    print(table)<br><br>
     Fungsi ini dibuat buat nampilkan menu utama dengan pilihan Pegawai, Customer, atau Keluar dalam bentuk tabel menggunakan PrettyTable.
<br><br>
baris 29-39:<br><br>
def login_pegawai():<br>
    nama = input("Masukkan Nama: ")<br>
    password = input("Masukkan Password: ")<br>
    if nama == "Ghen" and password == "1610":<br>
        print("Login berhasil!\nKerja Ghen jangan malas terus.")<br>
        return True<br>
    else:<br>
        print("Duh kok bisanya lupa")<br>
        return False<br><br>
fungsi ini dibuat untuk minta pegawai masukkan nama dan password.<br> 
Jika benar (nama "Ghen" dan password "1610"), login berhasil dan akan dikembalikan nilai True.<br>
Jika salah, muncul pesan error dan dikembalikan False.
<br><br>
Baris 42-56:<br><br>
def register_customer_fungsi():<br>
    print("Registrasi Customer:")<br>
    nama = input("Masukkan Nama: ")<br>
    alamat = input("Masukkan Alamat: ")<br>
    nik = input("Masukkan NIK KTP: ")<br>
    register_customer[nama] = {<br>
        'nama': nama,<br>
        'alamat': alamat,<br>
        'nik': nik<br>
    }<br>
    print("\nRegistrasi berhasil!, sekarang login pakai data yang sama.\n")<br>
    return nama, alamat, nik<br><br>
Fungsi ini buat customer untuk melakukan registrasi dengan memasukkan nama, alamat, dan NIK KTP. Habis data dimasukkan,<br> data customer disimpan di dictionary register_customer. Fungsi ini juga mengembalikan data customer yang terdaftar (nama, alamat, nik).
<br><br>
Baris 59-70:<br><br>
def login_customer(nama_terdaftar, alamat_terdaftar, nik_terdaftar):<br>
    print("Login Customer:")<br>
    nama = input("Masukkan Nama: ")<br>
    alamat = input("Masukkan Alamat: ")<br>
    nik = input("Masukkan NIK KTP: ")<br>
    if nama == nama_terdaftar and alamat == alamat_terdaftar and nik == nik_terdaftar:<br>
        print("Login berhasil!")<br>
        return True<br>
    else:<br>
        print("Duh salah\n")<br>
        return False<br><br>
Setelah registrasi, customer harus login kembali menggunakan data yang sama (nama, alamat, dan NIK).<br> Fungsi ini mencocokkan input customer dengan data yang terdaftar dan mengembalikan nilai True jika login berhasil.
<br><br>
Baris 73-78:<br><br>
def tampilkan_mobil():<br>
    table = PrettyTable()<br>
    table.field_names = ["No", "Nama Mobil", "Tarif per Hari (Rp)"]<br>
    for i, (mobil, tarif) in enumerate(mobil_tersedia.items(), start=1):<br>
        table.add_row([i, mobil, tarif])<br>
    print(table)<br><br>
  Untuk nampilkan daftar mobil yang tersedia dan tarif per hari dalam bentuk tabel pakai prettytable.<br>
  Setiap mobil dikasih nomor urut.
  <br><br>
  Baris 81-83:<br><br>
  def sewa_mobil(nama_customer):<br>
    print("\nDaftar Mobil yang Tersedia dan Tarifnya:")<br>
    tampilkan_mobil()<br>
    pilihan_mobil = int(input("Pilih mobil yang ingin disewa (masukkan nomor): "))<br>
    if 1 <= pilihan_mobil <= len(mobil_tersedia):<br>
        mobil_pilihan = list(mobil_tersedia.keys())[pilihan_mobil - 1]<br>
        lama_sewa = int(input(f"Berapa hari Anda ingin menyewa {mobil_pilihan}? "))<br>
        biaya_total = mobil_tersedia[mobil_pilihan] * lama_sewa<br>
        rental_data[nama_customer] =<br>
            'mobil': mobil_pilihan,<br>
            'lama': lama_sewa,<br>
            'biaya_total': biaya_total<br>
        }<br>
        del mobil_tersedia[mobil_pilihan]<br>
        print(f"Anda telah memilih {mobil_pilihan} untuk {lama_sewa} hari. Total biaya: Rp{biaya_total}")<br>
    else:<br>
        print("Mobil tidak tersedia. Kembali ke menu.")<br><br>
fungsi ini dipakai untuk proses penyewaan mobil. Customer milih mobil berdasarkan nomor urut,<br>
lalu menentukan lama penyewaan. Total biaya dihitung berdasarkan tarif harian.<br>
Data penyewaan disimpan di rental_data dan mobil dihapus dari mobil_tersedia.
<br><br>
Baris 107-119:<br><Br>
def kembalikan_mobil(nama_customer):<br>
    if nama_customer in rental_data:<br>
        mobil_dikembalikan = rental_data[nama_customer]['mobil']<br>
                mobil_tersedia[mobil_dikembalikan] = rental_data[nama_customer]['biaya_total'] // rental_data[nama_customer]['lama']<br>
          print(f"Mobil {mobil_dikembalikan} telah dikembalikan.")<br>
        del rental_data[nama_customer]<br>
        print("Pengembalian berhasil. Mobil telah kembali tersedia.")<br>
    else:<br>
        print("Anda belum menyewa mobil. Kembali ke menu utama.")<br>,<br>
Customer bisa ngembalikan mobil yang sudah disewa. Mobil yang dikembalikan ditambahkan kembali<br> 
ke mobil_tersedia dan data rental dihapus dari rental_data.
<br><br>
Baris 122-164:<br><br>
def customer_menu():<br>
    while True:<br>
    table = PrettyTable()<br>
        table.field_names = ["Pilihan", "Keterangan"]<br>
        table.add_row(["1.", "Ingin Melakukan Rental"])<br>
        table.add_row(["2.", "Mengembalikan Mobil"])<br>
        table.add_row(["3.", "Tidak Melakukan Rental"])<br>
        print(table)<br>
        pilihan = int(input("Apa yang ingin Anda lakukan? "))<br>
        if pilihan == 1:<br>
        nama_terdaftar, alamat_terdaftar, nik_terdaftar = register_customer_fungsi()<br>
        f login_customer(nama_terdaftar, alamat_terdaftar, nik_terdaftar):<br>
                print("Proses rental dapat dilanjutkan.\n")<br>
                table = PrettyTable()<br>
                table.field_names = ["Pilihan", "Keterangan"]<br>
                table.add_row(["1.", "Lihat Daftar Mobil dan Tarif"])<br>
                print(table)<br><br>
                opsi = int(input("Masukkan pilihan: "))<br>
                if opsi == 1:<br>
                    sewa_mobil(nama_terdaftar)<br>
                else:<br>
                    print("Pilihan tidak valid.")<br>
                break<br>
            else:<br>
                break<br>
                 elif pilihan == 2:<br>
            print("Anda memilih untuk mengembalikan mobil.")<br>
            nama = input("Masukkan nama anda untuk pengembalian: ")<br>
            kembalikan_mobil(nama)<br>
            elif pilihan == 3:<br>
            print("Anda memilih untuk tidak melakukan rental. Kembali ke menu utama.")<br>
            break<br>
        else:<br>
            print("Pilihan tidak valid. Silakan coba lagi.")<br><br>
    Menu untuk customer yang menawarkan pilihan untuk melakukan rental, mengembalikan mobil, atau keluar. Customer<br>
    yang ingin rental harus registrasi dan login terlebih dahulu.


        
