import unittest

from calculadora import soma

# https://docs.python.org/pt-br/3/library/unittest.html

#todas os testes dentro da classe deve iniciar com a palavra test
#se eu nao usasse o subtest eu nao saberia especificadamente onde teria ocorrido o erro (so saberia que o test passou ou nao segue exemplo abaixo)
#test_soma_varias_entradas (__main__.TestCalculadora) ... ok


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5,5),10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5,5),0)       

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):  # no caso tento essa linha a mais eu consigo ver qual dos testes falhou
                x , y ,saida = x_y_saida
                self.assertEqual(soma(x ,y),saida)

#testando as asserts que eu tinha criado la no codigo

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError): #Esse AssertionError foi porque eu definir la no codigo calculadora.py que fosse levantado caso X fosse diferente int ou float
            soma('11',5)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(11,'5')

if __name__ == "__main__" :
    unittest.main(verbosity=2)
