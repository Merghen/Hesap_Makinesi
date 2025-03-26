from abc import ABC, abstractmethod

class Islem(ABC):

    @abstractmethod
    def hesapla(self, x,y):
        pass


class Toplama(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):

        sonuc=x+y
        return sonuc

class Cikarma(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):

        sonuc=x-y
        return sonuc
    
class Caprma(Islem):

    def __init__(self):
        pass
        
    def hesapla(self, x,y):

        sonuc=x*y
        return sonuc

class Bolme(Islem):

    def __init__(self):
        pass
        
    def hesapla(self,x,y,kalanli=False):
        if(kalanli==True):
            sonuc=x/y
        else:
            sonuc = x//y
        
        return sonuc


