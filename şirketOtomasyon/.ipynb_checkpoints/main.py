import time
from smarket import *
urunNesne=SuperMarket()
print("""
1-Urun Ekle
2-Urun Sil
3-Stok Sorgula
4-Stok Sorgula(marka adi)
5-Toplam urun stok Sorgula
6-Son Kullanma tarihi gecenleri kaldir
7-Satis yap
8-İade Al
9-Gunluk Toplam musteri Sayisi
11.GÜNLÜK CİRO HESAPLA

----------------------------------------

12.KASAYI KAPAT

 ************************""")
while True:

    girdi = input("Seçim Yapın : ")

    if (girdi == "12"):

        print("---------------")

        print("Kasa Kapatıldı!")

        print("Program Sonlandırılıyor...")

        urunNesne.KasayiKapat()

        urunNesne.VeritabaniBaglantisiniKes()

        break

    elif (girdi == "1"):

        urunAdi = input("Ürün Adı : ")

        marka = input("Marka : ")

        fiyat = float(input("Fiyat : "))

        skt = input("Son Kullanma Tarihi : ")

        urunCesidi = input("Ürün Çeşidi : ")

        stok = int(input("Stok : "))

        print("Ürün Ekleniyor...")

        time.sleep(1)

        urun = Urun(urunAdi, marka, fiyat, skt, urunCesidi, stok)  # Her eleman ekleyeceğimizde bir nesne oluşturuyoruz.

        urunNesne.UrunEkle(urun)  # fonksiyonları kullanmak için tek bir SuperMarket class nesnesi oluşturmak yeterli.

        # UrunEkle fonksiyonunu kullanmak için her seferinde SuperMarket classı için nesne tanımlamaya gerek yok

        # Bu yüzden en başta urunNesne diye tanımlamamız yeterli.

        print("Ürün Eklendi!")

    elif (girdi == "2"):

        urunAdi = input("Silmek İstediğiniz Ürün Adını Girin : ")

        urunNesne.UrunSil(urunAdi)



    elif (girdi == "3"):

        urunAdi = input("Sorgulamak istediğiniz ürün adını girin : ")

        urunNesne.UrunAdinaGoreStokSorgula(urunAdi)

    elif (girdi == "4"):

        marka = input("Sorgulamak istediğiniz Marka adını girin :")

        urunNesne.MarkayaGoreStokSorgula(marka)

    elif (girdi == "5"):

        urunNesne.SuperMarketToplamUrunStoguSorgula()

    elif (girdi == "6"):

        girdi = input("Hangi Tarihten Öncesini Silmek İstiyorsunuz (Örn: 01.01.2018) : ")

        urunNesne.SonKullanmaTarihiGecenleriSil(girdi)

    elif (girdi == "7"):

        while True:

            girdi = input("Ürün Adı Girin (iptal : i | fiş : f): ")

            if (girdi == "i"):

                urunNesne.ilkGiris = True  # Sepeti iptal edersek, FisKes() teki gibi yine ilkGiris'i True yapıyoruz ki birdahaki müşteride ilk defa stoğu alacağı if'e girebilsin.

                break

            elif (girdi == "f"):

                print("Fiş Kesiliyor. Ödeme için teşekkürler!")

                urunNesne.FisKes()

                break

            else:

                urunNesne.SatisYap(girdi)



    elif (girdi == "8"):

        girdi = input("İade etmek istediğiniz ürünün adını girin : ")

        urunNesne.IadeAl(girdi)

    elif (girdi == "9"):

        urunNesne.GunlukToplamMusteriSayisi()

    elif (girdi == "10"):

        urunNesne.GunlukAlinanIadeSayisi()

    elif (girdi == "11"):

        urunNesne.GunlukCiroHesapla()

    else:

        print("Geçersiz İşlem!")

