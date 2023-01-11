import pytest
from pytest import mark

from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retornar_23(self):  # O método deve começar com test_ e o nome deve ser o mais verboso possivel
        entrada = "13/03/2000"  #Given-Contexto
        esperado = 23

        funcionario_test = Funcionario('Test', entrada, 1000)        
        resultado = funcionario_test.idade() # When-ação

        assert resultado == esperado #Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' #Given
        esperado = "Carvalho"

        lucas = Funcionario(entrada, '11/11/2000', 2000)
        resultado = lucas.sobrenome() #When

        assert resultado == esperado


    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000 #given
        esperado = 100

        funcionario_test= Funcionario('test', '11/11/1997', entrada_salario)
        resultado = funcionario_test.calcular_bonus() #when

        assert resultado == esperado #then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retonar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000   #given

            funcionario_test = Funcionario('test', '11/11/1997', entrada_salario)
            resultado = funcionario_test.calcular_bonus() # when

            assert resultado    #then