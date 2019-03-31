__author__ = "METE ÖZCAN"

while True:
    print ("Tren   (1)")
    print ("Araba   (2)")
    print ("Uçak (3)")
    print ("Gemi   (4)")
    print ("------------------------")
    print
    Ulasimaraci = input("Hangi ulaşım aracı ile seyahat etmek istersiniz? ... : ")
    İsim =  input ("Yolcu İsim: ")

    if Ulasimaraci == "1":
        print("Ulaşım aracınız şeçilmiştir... İyi yolculuklar dileriz...","Tren ile seyahat edeceksiniz...", İsim )
        print()
    elif Ulasimaraci == "2":
        print("Ulaşım aracınız şeçilmiştir... İyi yolculuklar dileriz..","Araba ile seyahat edeceksiniz...", İsim )
        print()
    elif Ulasimaraci == "3":
        print("Ulaşım aracınız şeçilmiştir... İyi yolculuklar dileriz..","Uçak ile seyahat edeceksiniz...", İsim )
        print()
    elif Ulasimaraci == "4":
        print("Ulaşım aracınız şeçilmiştir... İyi yolculuklar dileriz..","Gemi ile seyahat edeceksiniz...", İsim )
        print()
    else:
        print("Girdiğiniz ulaşım aracı geçersizdir.")
    break