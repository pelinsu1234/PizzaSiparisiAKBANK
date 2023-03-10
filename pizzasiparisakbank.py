import csv
from datetime import datetime



menu=open("menu.txt","w")
menu.write(""" 
           Lütfen Bir Pizza Tabani Seçiniz:
           1--Klasik Pizza--15tl
           2--Margarita--20tl
           3--Turk Pizza--25tl
           4--Sade Pizza--10tl
           Sos Seciniz :
           11--Zeytin--3tl
           12--Mantarlar--5tl
           13--Keci Peyniri--2tl
           14--Et--7tl
           15--Sogan--2tl
           16--Misir--2tl 
         Tesekkur ederiz!
         """)



class Pizza:
    def __init__(self):
         pass
    
    def get_description(self):
      return self.description

    def get_cost(self):
        return self.cost
    
class KlasikPizza(Pizza):
    fiyat= 15 
    description= "Klasik Pizza"
    def get_cost(self):
        return self.fiyat
    def get_description(self):
        return self.description

class MargaritaPizza(Pizza):
    fiyat = 20
    description = "Margarita Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.fiyat


class TurkPizza(Pizza):
    fiyat = 25
    description = "Turk Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.fiyat


class SadePizza(Pizza):
    fiyat = 10
    description = "Sade Pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.fiyat
    
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

    def get_description(self):
        return self.component.get_description() + " " + super().get_description()

class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytin ile"
        self.cost = 3

class Mantar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantar ile"
        self.cost = 5

class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peyniri ile"
        self.cost = 2

class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Et ile"
        self.cost = 7

class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Sogan ile"
        self.cost = 2

class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Misir ile"
        self.cost = 2

menu= open("menu.txt","r")
for i in menu:
    print(i,end="")

  


secimpizza= int(input("Lutfen sectiginiz pizzanin numarasini giriniz: "))


pizza = None
if secimpizza== 1:
        pizza = KlasikPizza()
      
elif secimpizza== 2:
        pizza = MargaritaPizza()
       
elif secimpizza == 3:
      pizza = TurkPizza()
    
elif secimpizza == 4:
        pizza = SadePizza()
       
else:
        print("Hatali secim yaptiniz.")
        exit()



secimsos= int(input("         Lutfen sectiginiz sosun numarasini giriniz: "))

if secimsos == 11:
        pizza = Zeytin(pizza)
elif secimsos == 12:
        pizza = Mantar(pizza)
elif secimsos == 13:
        pizza = KeciPeyniri(pizza)
elif secimsos == 14:
        pizza = Et(pizza)
elif secimsos == 15:
        pizza = Sogan(pizza)
elif secimsos == 16:
        pizza = Misir(pizza)
else:
        print("Hatali secim yaptiniz.")
        exit()

print(pizza.get_description())
print("Toplam ödeme: " + str(pizza.get_cost()) + "tl")

isim= input("İsminizi ve soyisminizi yazınız: ")
tc=input("Lütfen tc kimlik numaranızı giriniz: ")
kredikart=input("Lütfen kredi kartı numaranızı giriniz: ")
kredisifre=input("Lütfen kart şifrenizi girin: ")
siparistarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("Orders_Database.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow([isim,tc,kredikart, kredisifre,
                         str(pizza.get_description()), str(pizza.get_cost()), siparistarihi])






