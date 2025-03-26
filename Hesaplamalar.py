from abc import ABC, abstractmethod
import math

class Islem(ABC):

    @abstractmethod
    def hesapla(self):
        pass


class Toplama(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):
        """
            Toplama işlemini yapar

            Parametreler:

                x: işlem yapılacak 1. sayı
                y: işlem yapılacak 2. sayı

            Dönüş:
            float: İşlemin sonucu
        """

        sonuc=x+y
        return sonuc

class Cikarma(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):
        """
            Çıkarma işlemini yapar

            Parametreler:

                x: işlem yapılacak 1. sayı
                y: işlem yapılacak 2. sayı

            Dönüş:
            float: İşlemin sonucu
        """

        sonuc=x-y
        return sonuc
    
class Caprma(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):
        """
            Çarpma işlemini yapar

            Parametreler:

                x: işlem yapılacak 1. sayı
                y: işlem yapılacak 2. sayı

            Dönüş:
            float: İşlemin sonucu
        """

        sonuc=x*y
        return sonuc

class Bolme(Islem):

    def __init__(self):
        pass
        
    def hesapla(self,x,y,kalanli=False):
        """
            Bölme işlemini yapar

            Parametreler:

                x: işlem yapılacak 1. sayı
                y: işlem yapılacak 2. sayı
                kalanli: İşlemin kalanlı yapılıp yapılmayacağını tutar.

            Dönüş:
            float: İşlemin sonucu
        """

        if(kalanli==True):
            sonuc=x/y
        else:
            sonuc = x//y
        
        return sonuc


class Karakok(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x):
        """
            Karakök işlemini yapar

            Parametreler:

                x: işlem yapılacak sayı

            Dönüş:
            float: İşlemin sonucu
        """

        sonuc=math.sqrt(x)
        return sonuc

class Us_Alma(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):
        """
            Üs alma işlemini yapar

            Parametreler:

                x: işlem yapılacak 1. sayı
                y: işlem yapılacak 2. sayı

            Dönüş:
            float: İşlemin sonucu
        """

        sonuc=x**y
        return sonuc


class Mod(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):
        """
           Mod alma işlemini yapar

            Parametreler:

                x: işlem yapılacak 1. sayı
                y: işlem yapılacak 2. sayı

            Dönüş:
            float: İşlemin sonucu
        """

        sonuc=x%y
        return sonuc