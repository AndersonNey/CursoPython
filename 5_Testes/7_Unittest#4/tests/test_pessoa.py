

#mesmo o VS CODE reclamando eu consigo importa o modulo porque eu estou acrescentando o caminho do 
#modulo que eu quero importa dentro path do caminho em que esta esse arquivo

try:      #e isso aqui deve ser feito antes dos imports normais
    import sys
    import os 

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),'../src'
            )
        )
    )
except:
    raise

import unittest
from unittest.mock import patch   #para criar dados facks
from classe_pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    #esse metodo é sempre executado antes de cada teste
    # setUp()
    #esse metodo é sempre executado depois de cada teste
    # tearDown()

    def setUp(self):
        self.p1 = Pessoa('luiz','otavio')

    def test_pessoa_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.nome, 'luiz')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'otavio')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:  #to simulando que quando achar essa funcao falar que ela vai fazel tal coisa
            fake_request.return_value.ok = True    #to falando que a variavel return_value (isso seria a variavel 'resposta' la no outro arquivo)
                                                                                #vai ter um atributo 'ok' valendo True
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO' )
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:  
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERROR 404' )
            self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:  
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO' )
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERROR 404' )
            self.assertFalse(self.p1.dados_obtidos)

if __name__ == "__main__" :
    unittest.main(verbosity=2)






