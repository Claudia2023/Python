import random
import unittest

class Cucaracha:
    
    def __init__(self, cantidad):
        self.Cantidad = cantidad

    def Reproducir (self):
        nunrand = random.randint(1, 10)
        self.Cantidad += nunrand
        return nunrand

    def Aplastar (self):
        self.Cantidad -= 1
        return -1

    def Rociar (self):
        nunrand = random.randint(1, 5)
        self.Cantidad -= nunrand
        return -nunrand
        
class PruebasUnitarias(unittest.TestCase):
    def __init__(self, testname, arg1, arg2):
        super(PruebasUnitarias, self).__init__(testname)
        self._cucaracha = arg1
        self._cantInit = arg2
        
    def Test_Reproducir(self):
        reprod = self._cucaracha.Reproducir()
        #print("Test_Reproducir::::", self._cucaracha.Cantidad,reprod,'\n')
        self.assertEqual(self._cucaracha.Cantidad, (reprod + self._cantInit))
        
    def Test_Aplastar(self):
        ant = self._cucaracha.Cantidad
        aplast = self._cucaracha.Aplastar()
        #print("Test_Aplastar::::", self._cucaracha.Cantidad,aplast,'\n')
        self.assertEqual(self._cucaracha.Cantidad, (ant + aplast))        
    
    def Test_Rociar(self):
        ant = self._cucaracha.Cantidad
        rociar = self._cucaracha.Rociar()
        #print("Test_Rociar::::", self._cucaracha.Cantidad,rociar,ant,'\n')
        self.assertEqual(self._cucaracha.Cantidad, (ant + rociar))  

if __name__ == "__main__":
    CantCucarachas = 5
    Insepto = Cucaracha(CantCucarachas)
    suite = unittest.TestSuite()
    suite.addTest(PruebasUnitarias('Test_Reproducir', Insepto, CantCucarachas))
    suite.addTest(PruebasUnitarias('Test_Aplastar', Insepto, 0))
    suite.addTest(PruebasUnitarias('Test_Rociar', Insepto, 0))
    unittest.TextTestRunner(verbosity=2).run(suite)
