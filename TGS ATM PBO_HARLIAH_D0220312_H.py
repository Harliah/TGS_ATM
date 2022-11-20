print('Selamat datang di Atm Sederhana Kami')
print('Pilih option :')
print(' 1.Check Saldo ')
print(' 2.Tarik tunai ')
print(' 3.Setor tunai ')
option=int(input('Silahkan pilih option :'))
Saldo_anda=2000000
if option==1:
    print('uang anda sebesar Rp 2.000.000')
elif option==2:
    print('saldo anda berjumlah Rp.2000000,silahkan ambil')
    print(' 1. 500.000 ')
    print(' 2. 1.000.000 ')
    print(' 3. 2.000.000 ')
    option2=int(input('option:'))
    if option2==1:
       hasil=Saldo_anda-500000
       print('uang kamu sekarang berjumlah ',hasil)
    elif option2==2:
        hasil2=Saldo_anda-1000000
        print('uang kamu sekarang berjumlah',hasil2)
    elif option2==3:        
        hasil3=Saldo_anda-2000000
        print('uang kamu sekarang berjumlah',hasil3)
elif option==3:
    print('Saldo anda berjumlah Rp.2.000.000,mau tabung berapa')
    option3=int(input('masukkan jumlah uang anda:'))
    hasil4=Saldo_anda+option3
    print('jumlah saldo anda sekarang adalah',hasil4)
else:
    print("pilihan anda salah,silahkan ulangi lagi!!")
                
