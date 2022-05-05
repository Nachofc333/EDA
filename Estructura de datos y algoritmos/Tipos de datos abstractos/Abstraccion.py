'''
Un tipo abstracto de datos es un determinado objeto que trata de obtener un tipo de infomacion por ejmeplo int float etc.
Una estructura de datos es la manera en programacion en la que yo construyo y organizo
tipos complejos de datos son aquellos que estan formados por multiples componentes como list o diccionary
'''


class CreditCard:
    def __init__(self, customer, idCard, limit):

        self.__customer = customer
        self.__idCard = idCard
        self.__limit = limit
        self.__balance = 0



class complejo:  #clase para crear numeros complejos
    def __init__(self, Re=0, Im=0):
        self.Re = Re
        self.Im = Im

    def __str__(self):
        if self.Re == 0 and self.Im == 0:
            give = "0"
        elif self.Re == 0:
            give = str(self.Im) + "i"
        elif self.Im == 0:
            give = str(self.Re)
        else:
            give = "{} + {}i".format(self.Re, self.Im)
        return give

    def __add__(self, z):
        r = complejo()
        r.Re = self.Re + z.Re
        r.Im = self.Im + z.Im
        return r

    def __sub__(self, z):
        r = complejo()
        r.Re = self.Re - z.Re
        r.Im = self.Im - z.Re
        return r

    def mod(self):
        operacion = (self.Re**2 + self.Im**2)**0.5
        return operacion

z1 = complejo(3, 4)
z2 = complejo(8, 5)
print(z1.mod())
print(z1+z2)
print(z1)