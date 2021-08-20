class Empregado:
    'Classe base para empregados'
    contador = 0

    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
        Empregado.contador += 1
    
    def mostra_contador (self):
        print("Número de empregados: %d" % Empregado.contador)

    def mostra_empregado (self):
        print("Nome :",self.nome, ", Salário: ", self.salario)

"""
emp1 = Empregado("Antonio",9100)
emp2 = Empregado("Professor", 15000)
emp1.idade = 29
emp1.mostra_empregado()
emp2.mostra_empregado()
"""
emp1 = Empregado("Antonio",9100)
emp1.idade = 29
