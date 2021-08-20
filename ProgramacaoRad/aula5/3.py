class Pessoa:
    contador = 0

    def __init__(self, nome, idade, sexo):

        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        Pessoa.contador += 1

    def mostrar_pessoa(self):
        print("Nome: ", self.nome, " Idade: ", self.idade, " sexo: ", self.sexo)


pessoa1 = Pessoa("Antonio", 29, "M")
pessoa2 = Pessoa("Laura", 38, "F")

pessoa1.mostrar_pessoa()
print(pessoa1.contador)
