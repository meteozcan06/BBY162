__author__ = "Mete Özcan"
#Adam Asmaca Oyunu
print("Adamasmaca Oyununa Hoşgeldiniz..")
print("Konumuz Türkiye\' nin 81 ili")

import random

secileNil = random.choice(['adana','adıyaman','afyon','ağrı','amasya','ankara','antalya','artvin','aydın','balıkesir','bilecik',\
                          'bingöl','bitlis','bolu','burdur','bursa','çanakkale','çankırı','çorum','denizli','diyarbakır','edirne',\
                          'elazığ','erzincan','erzurum','eskişehir','gaziantep','giresun','gümüşhane','hakkari','hatay','ısparta',\
                          'mersin','istanbul','izmir','kars','kastamonu','kayseri','kırklareli','kırşehir','kocaeli','konya',\
                          'kütahya','malatya','manisa','kahramanmaraş','mardin','muğla','muş','nevşehir','niğde','ordu','rize',\
                          'sakarya','samsun','siirt','sinop','sivas','tekirdağ','tokat','trabzon','tunceli','şanlıurfa','uşak',\
                          'van','yozgat','zonguldak','aksaray','bayburt','karaman','kırıkkale','batman','şırnak','bartın',\
                          'ardahan','ığdır','yalova','karabük','kilis','osmaniye','düzce'])
kalanCan = 6
iller = []
altCizgi = "__"

for kelime in secileNil:
    iller.append(altCizgi)
print(iller)
while kalanCan > 0:
    i = 0
    yazılan_harf = input("\nTürkiye\'nin illerini tahmin edebilmek için bir harf yazınız: ").lower()
    if yazılan_harf in secileNil:
        for kontrol in secileNil:
            if secileNil[i] == yazılan_harf:
                iller[i] = yazılan_harf
            i += 1
        print("")
        print(iller)
        print("\n Tebrikler doğru tahmin! ")
    else:
        kalanCan -= 1
        print("")
        print(iller)
        print("\n Malesef yanlış tahmin!")
        print("\nKalan can = %s" %kalanCan)
    if kalanCan == 0:
        print("Oyun Bitti! Doğru cevap: %s" %secileNil)
        break
    if altCizgi not in iller:
        print("\nKazandınız!")
        break

