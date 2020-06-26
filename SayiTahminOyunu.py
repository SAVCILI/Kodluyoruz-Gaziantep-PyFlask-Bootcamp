import random


def SayiTahmin():
    sayi=random.randint(0,100)
    tahmin=-1
    count=0



   


    while  tahmin !=sayi:

        tahmin_str=input("0 ile 100 arasında bir sayı tahmin ediniz: ")
        tahmin=int(tahmin_str)
        count+=1  

        if tahmin<0:
            print("Lütfen Pozitif Bir Sayı Giriniz:")

        elif tahmin<sayi:
            print("Düşük bir tahmin tekrar dene")

        elif tahmin>sayi:
            print("Yüksek bir tahmin tekrar dene")
        

        else:
            print("TEBRİKLER :) SAYIYI ", count, "TAHMİNDE BİLDİNİZ:)")

    

    tekrar()





def tekrar():
    devam_etsin_mi=input("Tekrar Sayı Tahmin Etmek İster misin? 'Evet' için Y,'Hayır' için N yazınız :)")

    if devam_etsin_mi.upper()=='Y':
        SayiTahmin()
    elif devam_etsin_mi.upper()=='N':
        print("Yine Bekleriz:)")
    else:
        again()

SayiTahmin()

