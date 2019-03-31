#dortgen_alan_hesapla_v1
def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) * float(yukseklik)
    print("Alan :", alan)
    return alan


gen = input("Genişlik : ")

yuk = input("Yükseklik : ")

dikdortgenAlan(gen, yuk)
#daire_alan_hesapla_v1
def daireAlan(yaricap):
    alan = float(yaricap) * float(yaricap) * 3.14
    print("Alan :", alan)
    return alan


r = input("Yarıçapı Gir : ")

daireAlan(r)
#dortgen_alanı_hesapla_v2
def dikdortgenAlan(genislik, yukseklik):
    alan = float(genislik) **2 * float(yukseklik) **2
    print("Alan :", alan)
    return alan


gen = input("Genişlik :")

yuk = input("Yükseklik :")

dikdortgenAlan(gen, yuk)
#daire_alanı_hesapla_v2
def daireAlan(yaricap):
    alan = (float(yaricap) * float(yaricap)) **2 * 3.14
    print("Alan :", alan)
    return alan


r = input("Yarıçapı Gir : ")

daireAlan(r)