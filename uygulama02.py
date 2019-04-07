__author__ = "Mete Özcan"
#Test Uygulaması
print("Soru-cevap oyunumuza hoşgeldiniz")
input("Başlamak için her hangi bir şey yazınız= ")
print("Oyunumuz Başlıyor")
Sorular = ['Yedi renkten oluşan gökkuşağının ortasındaki renk hangisidir?',\
           'Aspirinin hammaddesi olan ağaç hangisidir?',\
           'Her 100 yılda 7 cm eğilmekte olan Pisa Kulesi hangi yöne doğru eğilmektedir?',\
           'Formik aside adını veren formika latincede hangi hayvandır?',\
           'İnsanlarla diyalog kurmak ve yeni bilgileri öğrenmek üzere tasarlanan robot "Kirobo Noel Baba\'dan ne istersin?" sorusuna ne yanıt vermiştir?']
Cevaplar = ['C', 'B', 'D', 'A', 'C']
cevapA = ['Mavi',\
          'Çam',\
          'Kuzey',\
          'Karınca',\
          'Arkadaş']
cevapB = ['Sarı',\
          'Söğüt',\
          'Batı',\
          'Kokarca',\
          'Ekmek']
cevapC = ['Yeşil',\
          'Meşe',\
          'Doğu',\
          'Arı',\
          'Oyuncak']
cevapD = ['Kırmızı',\
          'Gürgen',\
          'Güney',\
          'Örümcek',\
          'Pilav']
Puan=0
for i in range(len(Sorular)):
    print("sorular"+str(i+1)+":"+Sorular[i])
    print("A) " + cevapA[i])
    print("B) " + cevapB[i])
    print("C) " + cevapC[i])
    print("D) " + cevapD[i])
    cevap = input("Cevabınız: ")
    if (Cevaplar[i] == cevap.upper()):
        Puan +=1
print("Testimiz Bitmiştir")
print("Aldığınız puan: "+str(int((Puan/len(Sorular)) * 100)))