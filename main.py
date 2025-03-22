# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 17:09:27 2025

@author: omer
"""


aktif_islemler={"toplama":"1",
                "cikarma":"2",
                "carpma":"3",
                "bolme":"4"
                }

while(True):
    
    islem = input("İşlem seç \n- toplama için: '1'\n- çıkarma için: '2' \n- çarpma için: '3' \n- bölme için: '4' \n- çıkmak için 'x' tuşuna basınız ").strip().lower()
    if(islem in aktif_islemler.values()):
        
        try:
            x = float(input("Birinci sayıyı gir: "))
            y = float(input("İkinci sayıyı gir: "))
            
            print(f"Seçilen değerler {x} ve {y}")
            break
        except Exception:
            print("Lütfen bir sayı gir.")
        
    elif(islem=="x"):
        print("Çıkış işlemi gerçekleştirildi.")
        break
    else:
        print("Lütfen geçerli bir işlem giriniz.")
       
        
    


    
        