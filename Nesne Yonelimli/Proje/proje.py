import time
import random
 
class Kumanda ():
    def __init__(self,tv_durum = "Kapalı",tv_ses= 0,kanallar=["TRT1"],kanal="TRT1"):
 
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanallar = kanallar
        self.kanal = kanal
    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon Zaten Açık...")
        else:
            print("Televizyon Açılıyor...")
        self.tv_durum = "Açık"
    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon Zaten Kapalı...")
        else:
            self.tv_durum = "Kapalı"
    def ses_ac(self):
        if (self.tv_ses == 100):
            print("Ses maksimum düzeyde")
        else:
            print("Ses birer birer yükseliyor")
            self.tv_ses += 1
    def ses_kıs(self):
        if (self.tv_ses == 0):
            print("Ses minimumda")
        else:
            print("Ses kısılıyor...")
            self.tv_ses -= 1
    def ses_kapat(self):
        self.tv_ses = 0
        print("ses kapatılıyor...")
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanallar.append(self.kanal_ismi)
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanallar)-1)
 
        self.kanal = self.kanallar(rastgele)
 
        print("Şu anki kanal:" ,self.kanal)
    def __len__(self):
        return len(self.kanallar)
    def __str__(self):
        return "Tv durumu : {}/nTv sesi : {}/n".format(self.tv_durum,self.tv_ses)
 
print("""
Televizyon uygulaması...
1. Tv aç
2. Tv kapat
3. Ses aç
4. Ses kıs
5. Ses kapat
6. Kanal ekle
7. Kanal sayısı öğrenme
8. Rastgele kanal
9. Televizyon ses bilgisi
 
Çıkış için q ya basınız...
""")
 
kumanda = Kumanda()
 
while True:
    işlem = (input("İşlemi seçiniz"))
    if işlem == "q":
        break
    else:
 
        if işlem == "1":
            kumanda.tv_ac()
        elif işlem == "2":
            kumanda.tv_kapat()
        elif işlem == "3":
            kumanda.ses_ac()
        elif işlem == "4":
            kumanda.ses_kıs()
        elif işlem == "5":
            kumanda.ses_kapat()
        elif işlem == "6":
            eklenecek_kanal = input("Hangi kanalları eklemek istersiniz?(Kanal isimlerini virgül ile ayırarak girin.")
            eklenecek_kanallar = eklenecek_kanal.split(",")
            for eklenecekler in eklenecek_kanallar:
                kumanda.kanal_ekle(eklenecekler)
                print(kanal_ekle(eklenecekler))
        elif işlem == "7":
            len(kumanda)
        elif işlem == "8":
            kumanda.rastgele_kanal()
        elif işlem == "9":
            print(kumanda)
        else:
            print("geçersiz işlem...")