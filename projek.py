import os
from linkedlist import LinkedList
myLink = LinkedList(
    ['mouse', 6, 'baru'], 
    ['monitor', 5, 'bekas'],
    ['kabel LAN', 10, 'bekas'],
    ['komputer', 3, 'baru'],
    ['server', 1, 'bekas']
    )

class inventaris:
    def __init__(self):
        os.system("cls")
        self.data = []
        # self.data = 
    def tambah(self):
        # self.show()
        global myLink 
        os.system('cls')
        print('\tPenginputan Data Barang')
        print('-'*30)
        data = input('Masukkan data Barang baru: ')
        Jumlah = int(input('Masukkan Jumlah: '))
        kondisi = str(input('Masukkan Kondisi: '))
        myLink.InsertAtEnd([data, Jumlah, kondisi])
        self.program()

    def show(self):
        global myLink
        os.system('cls')
        print('No','\tJumlah','\tNama Barang','\tKondisi')
        for i in range(len(myLink)):
            print(f"{i+1}","\t",myLink[i][1],'\t',myLink[i][0],'\t\t',myLink[i][2])

    def showlist(self):
        global myLink
        os.system('cls')
        print('No','\tJumlah','\tNama Barang','\tKondisi')
        for i in range(len(myLink)):
            print(f"{i+1}","\t",myLink[i][1],'\t',myLink[i][0],'\t\t',myLink[i][2])
        input()
        self.program()

    def showpinjam(self):
        os.system('cls')
        print('\tDaftar Riwayat Peminjaman')
        print('='*20)
        print('No','\tjumlah','\tNama Barang')
        for i in range(len(self.data)):
            print(f'{i+1}','\t',self.data[i][1],'\t',self.data[i][0],'\t',self.data[i][2])
        input()
        self.program()

    def hapus(self):
        self.show()
        global myLink
        index = int(input('Masukkan No yang akan dihapus: '))-1
        n = input('Apakah anda benar ingin menghapus? [y] and [n]: ').lower()
        if n == 'y':
            myLink.DeleteAtIndex(index)
            input()
            self.program()
        else:
            self.program()

    def changeList(self):
        global myLink
        if len(myLink) == 0:
            print('List Not identified')
            input()
            self.program()
        else:
            self.show()
            index = int(input('Masukkan No data: '))-1
            n = input('Apakah anda benar ingin mengubah? [y] and [n]: ').lower()
            if n == 'y':
                data = str(input('Masukkan nama barang baru: '))
                Jumlah = int(input('Masukkan jumlah baru: '))
                kondisi = input('Masukkan kondisi Terbaru: ')
                myLink.ChangeElementByIndex(index,[data,Jumlah,kondisi])
                self.program()
            else:
                self.program()
        # return ubah
    def screen(self):
        print (f"""
        \t Welcome To MyAppas Inventaris Lab
        {'-'*50}
        """)
        input("\n Tekan [ENTER] untuk melanjutkan")

    def peminjaman(self):
        self.show()
        print(f"""
            Jangan Lupa Melakukan Pengecekan Terhadap Kondisi Barang
                {'='*20}     
        """)
        idxbarang=int(input('Masukkan No yang akan dipinjam: '))-1
        n = input('Apakah anda benar ingin meminjam? [y] and [n]: ').lower()
        if n == 'y':
            jumlah = int(input("Jumlah yang dipinjam: "))
            nama = myLink[idxbarang][0]
            kondisi = myLink[idxbarang][2]
            self.data.append([myLink[idxbarang][0],jumlah,myLink[idxbarang][2]])
            ubah = myLink[idxbarang][1]-jumlah
            myLink.ChangeElementByIndex(idxbarang,[nama,ubah,kondisi])
            self.program()
        else:
            self.program()

    def pengembalian(self):
        os.system('cls')
        print('\tDaftar Riwayat Peminjaman')
        print('='*20)
        print('No','\tJumlah','\tNama Barang', '\tKondisi')
        for i in range(len(self.data)):
            print(f'{i+1}','\t',self.data[i][1],'\t',self.data[i][0],'\t',self.data[i][2])
        print(f"""
            Jangan Lupa Melakukan Pengecekan Terhadap Kondisi Barang
                {'='*20}     
        """)

        idxbarang=int(input('Masukkan No yang akan dikembalikan: '))-1
        j = 0
        for i in myLink:
            if i[0] == self.data[idxbarang][0]:
                break
            j += 1
        n = input('Apakah anda benar ingin mengembalikan? [y] and [n]: ').lower()
        if n == 'y':
            jumlah = int(input("Jumlah yang dikembalikan: "))
            nama = self.data[idxbarang][0]
            kondisi = self.data[idxbarang][2]
            ubah = myLink[j][1]+jumlah
            self.data[idxbarang][1] -= 1 
            myLink.ChangeElementByIndex(j,[nama,ubah,kondisi])
            self.program()
        else:
            self.program()
    
    def program(self):
        os.system('cls')
        print('\tInventaris Labortaorium')
        print('='*45)
        print("""
            [1] Input Barang
            [2] Hapus Barang
            [3] Edit Barang
            [4] Lihat barang
            [5] Peminjaman
            [6] Pengembalian
            [7] Riwayat peminjaman
            [8] Keluar
        """)
        n = int(input('Masukkan No. Menu : '))
        self.menu(n)

    def menu(self,n):
        os.system('cls')
        if n == 1:
            self.tambah()
        elif n == 2:
            self.hapus()
        elif n == 3:
            self.changeList()
        elif n == 4:
            self.showlist()
        elif n == 5:
            self.peminjaman()
        elif n == 6:
            self.pengembalian()
        elif n == 7:
            self.showpinjam()
        elif n == 8:
            pass
        else :
            print("Masukan Salah, Mohon masukan pilihan yang benar!!!")
            input("Tekan [ENTER] untuk kembali")
            self.program()

myinv = inventaris()
myinv.program()