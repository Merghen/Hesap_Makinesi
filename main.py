# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 17:09:27 2025

@author: omer
"""

import Hesaplamalar

class Arayuz():

    aktif_islemler={"1":Hesaplamalar.Toplama(),
                "2":Hesaplamalar.Cikarma(),
                "3":Hesaplamalar.Caprma(),
                "4":Hesaplamalar.Bolme(),
                "5":Hesaplamalar.Karakok(),
                "6":Hesaplamalar.Us_Alma(),
                "7":Hesaplamalar.Mod()
                }
    islem=None


    def __init__(self):
        pass

    def sonucu_getir(self,islem,x,y=None):
        """
            Arayüzde seçilen işlemi alır ve hesaplamayı yapar.

            Parametreler:
                islem: Yapılacak işlemin türü.
                x: işlem yapılacak 1. sayı
                y: işlem yapılacak 2. sayı

            Dönüş:
            float: İşlemin sonucu
        """

        # Eğer işlem bölme ise:
        if(islem=="4"):
            kalanli_mi=input("Kalanlı Bölme için: '1' \nKalansız Bölme için: '2' tuşuna basınız  ").strip().lower()

            if(kalanli_mi=="1"):
                kalanli_mi=True
                        
            elif(kalanli_mi=="2"):    
                kalanli_mi=False

            else:
                print("Geçersiz işlem.")
                return None
                
            sonuc=Arayuz.aktif_islemler[islem].hesapla(x, y,kalanli_mi)

        #Eğer seçilen işlem karakök ise tek sayı gönder.
        if(islem=="5"):
            sonuc=Arayuz.aktif_islemler[islem].hesapla(x)

        # Toplama, Çıkarma Çarpma, Üs ve Mod alma işlemleri için:        
        else:
            sonuc=Arayuz.aktif_islemler[islem].hesapla(x, y)
                    
        return sonuc    

    def arayuz_getir(self):
        """
            Arayüzü dönderir.
        """
        
        while(True):  
            Arayuz.islem = input("İşlem seç \n- toplama için: '1'\n- çıkarma için: '2' \n- çarpma için: '3' \n- bölme için: '4'  \n- karakök için: '5'  \n- üs almak için:'6'  \n- mod almak için: '7' \n- çıkmak için 'x' tuşuna basınız ").strip().lower()
            if(Arayuz.islem in Arayuz.aktif_islemler.keys()):
                
                try:
                    # Eğer karakök işlemin seçildiyse 2. bir sayıya gerek yok.
                    if(Arayuz.islem=="5"):
                        
                        x = float(input("Karakökü alınacak sayıyı giriniz: "))
                        print(f"Seçilen değer {x}")
                        sonuc=self.sonucu_getir(islem=Arayuz.islem,x=x)

                    # Diğer tüm işlemler için 2 sayı gerekli.
                    else:
                        x = float(input("Birinci sayıyı gir: "))
                        y = float(input("İkinci sayıyı gir: "))
                        print(f"Seçilen değerler {x} ve {y}")
                        sonuc=self.sonucu_getir(islem=Arayuz.islem,x=x,y=y)
                    
                    
                    print(f"İşleminin sonucu: {sonuc}")    
                
                    break
                except Exception:
                    print("Lütfen bir sayı gir.")
            #Çıkış işlemi    
            elif(Arayuz.islem=="x"):
                print("Çıkış işlemi gerçekleştirildi.")
                break
            else:
                print("Lütfen geçerli bir işlem giriniz.")


arayuz=Arayuz()
arayuz.arayuz_getir()

        

    
        