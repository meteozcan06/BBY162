__author__ = "Mete Özcan"
#Test Uygulaması
print("Soru-cevap oyunumuza hoşgeldiniz")
x = input("Başlamak için her hangi bir şey yazınız= ")
if x == " ":
    print("Oyunumuz Başlıyor")
puan=0
Soru1 = input('Yedi renkten oluşan gökkuşağının ortasındaki renk hangisidir?: ')
Soru1=Soru1.lower()
print(Soru1)
if Soru1 == "yeşil":
    print("Cevabınız doğru")
    puan += 20
else:print("Cevabınız yanlış doğru cevap yeşil.")
Soru2 = input('Aspirinin hammaddesi olan ağaç hangisidir?: ')
Soru2=Soru2.lower()
print(Soru2)
if Soru2 == "söğüt":
    print("Cevabınız doğru")
    puan += 20
else:print("Cevabınız yanlış doğru cevap söğüt.")
Soru3 = input('Her 100 yılda 7 cm eğilmekte olan Pisa Kulesi hangi yöne doğru eğilmektedir?: ')
Soru3=Soru3.lower()
print(Soru3)
if Soru3 == "güney":
    print("Cevabınız doğru")
    puan += 20
else:print("Cevabınız yanlış doğru cevap Güney")
Soru4 = input('Formik aside adını veren formika latincede hangi hayvandır?: ')
Soru4=Soru4.lower()
print(Soru4)
if Soru4 == "karınca":
    print("Cevabınız doğru")
    puan += 20
else:print("Cevabınız yanış doğru cevap karınca")
Soru5 = input('İnsanlarla diyalog kurmak ve yeni bilgileri öğrenmek üzere tasarlanan robot "Kirobo Noel Baba\'dan ne istersin?" sorusuna ne yanıt vermiştir?: ')
Soru5=Soru5.lower()
print(Soru5)
if Soru5 == "oyuncak":
    print("Cevabınız doğru")
    puan += 20
else:print("Cevabınız yanlış doğru cevap oyuncak")
#Test Sonu
print("Testi tamamladınız, aldığınız puan: "+str(puan*1))