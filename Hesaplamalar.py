from abc import ABC, abstractmethod

class Islem(ABC):

    @abstractmethod
    def hesapla(self, x,y):
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


