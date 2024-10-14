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
from prettytable import PrettyTable
