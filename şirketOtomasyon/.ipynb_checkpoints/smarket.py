import sqlite3
import sys
print(sys.path)


class Urun():
    def __init__(self, uAdi, marka, fiyat, skt, uCesidi, stok):
        self.uAdi = uAdi
        self.marka = marka
        self.fiyat = fiyat
        self.skt = skt
        self.uCesidi = uCesidi
        self.stok = stok

    def __str__str(self):
        return self.stok


class SuperMarket():
    def __init__(self):
        self.veritabaninaBaglan()
        self.ilkGiris = True  # init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.
        self.gunlukToplamMusteri = 0  # init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.
        self.toplamfiyat = 0  # init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.
        self.toplamCiro = 0
        self.gunlukToplamIade = 0  # init fonksiyonu ilk çalışan fonksiyon olduğu için buraya yazdım. programın başında çalışmasını istiyorum.

    def veritabaninaBaglan(self):
        self.baglanti = sqlite3.connect("veriler.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS veriler(UrunAdi TEXT,Marka TEXT,Fiyat REAL,SKT TEXT,UrunCesidi TEXT,Stok INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiKes(self):
        self.baglanti.close()

    def urunEkle(self, urun):
        sorgu = "INSERT INTO veriler VALUES(?,?,?,?,?,?)"
        self.cursor.execute(sorgu, (urun.uAdi, urun.marka, urun.fiyat, urun.skt, urun.uCesidi, urun.stok))
        self.baglanti.commit()

    def urunSil(self, isim):
        sorgu2 = "SELECT * FROM veriler WHERE UrunAdi=?"
        self.cursor.execute(sorgu2, (isim))
        silinecekUrunler = self.cursor.fetchall()
        if (len(silinecekUrunler) == 0):
            print("Böyle bir ürün bulunmuyor")
        else:
            print("ürün silindi")
        sorgu = "DELETE * FROM veriler WHERE UrunAdi=?"
        self.cursor.execute(sorgu, (isim))
        self.baglanti.commit()

    def UrunAdinaGoreStokSorgula(self, isim):
        sorgu = "SELECT * FROM veriler WHERE UrunAdi=?"
        self.cursor.execute(sorgu, (isim))
        urunler = self.cursor.fetchall()
        if (len(urunler) == 0):
            print("stokta boyle bir urun yok")
        else:
            toplamurun = 0
            for i in urunler:
                toplamurun += i[5]
            print(toplamurun)

    def MarkayaGoreStokSorgula(self, marka):

        sorgu = "SELECT * FROM veriler WHERE Marka = ?"

        self.cursor.execute(sorgu, (marka,))

        markaurunleri = self.cursor.fetchall()

        if (len(markaurunleri) == 0):

            print("Stokta böyle bir marka ürünü bulunmuyor.")

        else:

            toplammarkaurunu = 0

            for i in markaurunleri:
                toplammarkaurunu += i[5]

            print("{} Markasına ait toplamda {} ürün mevcut".format(marka, toplammarkaurunu))

    def SuperMarketToplamUrunStoguSorgula(self):
        sorgu = "SELECT * FROM veriler"
        self.cursor.execute(sorgu)
        toplamstok = self.cursor.fetchall()
        if (len(toplamstok) == 0):

            print("Stokta ürün bulunmuyor.")

        else:

            toplamurunstogu = 0
            for i in toplamstok:
                toplamurunstogu += i[5]
            print("Bulunan tüm ürünlerin toplam stoğu {}'dir".format(toplamurunstogu))

    def tarihiGecenleriSil(self,isim):  # bu fonksiyonu sadece SonKullanmaTarihiGecenleriSil() fonksiyonunda kullanmak için oluşturdum.
        sorgu = "DELETE FROM veriler WHERE UrunAdi = ?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()

    def sonKullanmaTarihiGecenleriSil(self, isim):
        sorgu = "SELECT * FROM veriler"
        self.cursor.execute(sorgu)
        butunurunler = self.cursor.fetchall()
        if (len(toplamstok) == 0):
            print("Stokta ürün bulunmuyor.")

        else:
            for i in butunurunler:
                sktListesi = i[3].split('.')
                tarihListesi = tarih.split('.')
                if (tarihListesi[2] > sktListesi[2]):
                    self.tarihiGecenleriSil(i[0])
                elif (tarihlistesi[2] == sktlistesi[2] and tarihlistesi[1] > sktlistesi[1]):  # Eğer yıllar eşitse aya bakıyorum. Girdiğim ay'dan düşükse girip sil
                    self.TarihiGecenleriSil(i[0])
                elif (tarihlistesi[2] == sktlistesi[2] and tarihlistesi[1] == sktlistesi[1] and tarihlistesi[0] > sktlistesi[0]):  # Eğer yıllar ve aylar eşitse güne bakıyorum. Girilen günden küçükse girip sil
                    self.TarihiGecenleriSil(i[0])


    def satisYap(self, isim):
        self.satisisim = isim
        sorgu = "SELECT * FROM veriler WHERE UrunAdi=?"
        self.cursor.execute(sorgu, (isim))
        urun = self.cursor.fetchall()
        if (len(urun) == 0):
            print("bu ürün bulunmuyor")
        else:
            if (self.ilkgiris):
                self.urunstok = urun[0][5]
                self.urunstok -= 1
                self.toplamfiyat += urun[0][2]
        print("Ürün Sepetinize Eklendi!")
        self.ilkGiris = False  # Burda False yapıyorum ki birdaha girmesin. Taa ki fiş kesilene kadar. Her fiş kesiminde ürün stoğunu güncelleyecek.


# Tekrardan satis yapılacağı zaman FisKes metodunda True yaptığımız için tekrar satış yapacağımızda yine ilk defasında 1 defa giriyor if'e.

def fisKes(self):
    sorgu = "UPDATE veriler SET Stok=? WHERE UrunAdi=?"
    self.cursor.execute(sorgu, (self.urunstok, self.satisisim))
    self.baglanti.commit()
    print("Toplam Tutar : {} TL".format(self.toplamfiyat))
    self.gunlukToplamMusteri += 1
    self.toplamCiro += self.toplamFiyat
    self.ilkgiris = True
    self.toplamfiyat = 0


def GunlukToplamMusteriSayisi(self):
    print("Bugün toplam {} müşteriye hizmet verdiniz.".format(self.gunlukToplamMusteri))


def GunlukCiroHesapla(self):
    if (self.toplamCiro > 0):
        print("-----------")
        print("Kârdasınız!")

    elif (self.toplamCiro < 0):
        print("-------------")
        print("Zarardasınız!")
        print("Günlük Toplam Cironuz : {} TL".format(self.toplamCiro))


def iadeAl(self, isim):
    sorgu = "SELECT *FROM veriler WHERE UrunAdi=?"
    self.cursor.execute(sorgu, (isim))
    urunler = self.baglanti.fetchall()
    stok = urunler[0][5]
    stok += 1
    self.toplamCiro -= urunler[0][2]
    sorgu2 = "UPDATE veriler SET Stok WHERE UrunAdi=?"
    self.cursor.execute(sorgu2, (stok, isim))
    self.baglanti.commit()
    print("iade alindi tesekkurler")
    self.gunlukToplamIade += 1


def GunlukAlinanIadeSayisi(self):
    print("Bugün Toplam {} İade Aldınız.".format(self.gunlukToplamIade))


def kasayiKapat(self):
    baglanti2 = sqlite3.connect("gunlukVeriler.db")
    cursor2 = baglanti2.cursor()
    sorgu = "CREATE TABLE IF NOT EXISTS gunlukVeriler(GunlukToplamMusteri INT,GunlukToplamCiro INT,GunlukToplamIade INT)"
    cursor2.execute(sorgu)
    baglanti2.commit()
    sorgu2 = "INSERT INTO gunlukVeriler VALUES(?,?,?)"
    cursor2.execute(sorgu2, (self.gunlukToplamMusteri, self.toplamCiro, self.gunlukToplamIade))
    baglanti2.commit()
    self.gunlukToplamMusteri = 0
    self.toplamCiro = 0
    self.gunlukToplamIade = 0


















