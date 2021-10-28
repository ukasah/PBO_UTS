#Konsep Polimorfisme dan Turunan
class Saldo:
    def __init__(self,umum,tabungan):
        self.umum = umum
        self.tabungan = tabungan

    def printname(self):
        print(self.umum)
        print(self.tabungan)
    
    def tambah(self, n, opsi):
        if opsi == 1:
            self.umum = self.umum + n
        elif opsi == 2:
            self.tabungan = self.tabungan + n

    def ambil(self, n, opsi):
        if opsi == 1:
            if (self.umum - n < 0):
                print("Pengambilan saldo tidak dapat dilakukan!")
                return
            self.umum = self.umum - n
        elif opsi == 2:
            if (self.tabungan - n < 0):
                print("Pengambilan saldo tidak dapat dilakukan!")
                return
            self.tabungan = self.tabungan - n

class Info(Saldo):
    def __init__(self, umum, tabungan):
        super().__init__(umum, tabungan)

    def tampilantambah(self):
        print("Saldo Umum Anda Saat Ini Adalah: Rp.",self.umum,"-")
        print("Saldo Tabungan Anda Saat Ini Adalah: Rp.",self.tabungan,"-")

    def jenisSaldo(self):
        print("==========================================")
        print("1. Umum")
        print("2. Tabungan")
        print("==========================================")

class Tambah(Saldo):
    def __init__(self, umum, tabungan):
        super().__init__(umum, tabungan)

    def tampilantambah(self):
         print("Saldo Umum Anda Saat Ini Adalah: Rp.",self.umum,"-")


class Ambil(Saldo):
    def __init__(self, umum, tabungan):
        super().__init__(umum, tabungan)

    def tampilanambil(self):
        print("Saldo Umum Anda Saat Ini Adalah: Rp.",self.umum,"-")
        print("Saldo Umum Anda Saat Ini Adalah: Rp.",self.tabungan,"-")


# antar muka program
pilihan = None
opsi_saldo = None
saldo_umum = 0
saldo_tabungan = 0
x = Saldo(saldo_umum,saldo_tabungan)
x = Info(saldo_umum,saldo_tabungan)
saldo_umum = None
saldo_tabungan = None
while True:

    print("== Aplikasi Pencatatan Uang Digital ==")
    print("1. Informasi Saldo")
    print("2. Tambah Saldo")
    print("3. Ambil Saldo")
    print("4. Keluar")
    print("=======================================")
    pilihan=int(input("Silahkan Pilih: "))
    if pilihan == 1:
        x.tampilantambah()

    elif pilihan == 2:
        x.tampilantambah()
        x.jenisSaldo()
        opsi_saldo=int(input("Pilih Penyimpanan: "))
        jumlah = int(input("Nominal yang akan ditambahkan: "))
        x.tambah(jumlah, opsi_saldo)
        print("Penambahan saldo sebesar Rp." + str(jumlah) + ", - berhasil!")
        x.tampilantambah()

    elif pilihan == 3:
        x.tampilantambah()
        x.jenisSaldo()
        opsi_saldo=int(input("Pilih Penyimpanan: "))
        jumlah = int(input("Nominal yang akan ditarik: "))
        x.ambil(jumlah, opsi_saldo)
        print("Pengambilan saldo sebesar Rp." + str(jumlah) + ", - berhasil!")
        x.tampilantambah()

    elif pilihan == 4:
        break
    else:
        print("== Masukkan pilihan yang benar (1,2,3,4) ==")