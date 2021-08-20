class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def get_idade(self):
        print("A idade da pessoa é ", self.idade)


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome='', idade=0):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf


class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome='', idade=0):
        Pessoa.__init__(self, nome, idade)
        self.cnpj = cnpj


pessoa = Pessoa()
Pessoa.__init__(pessoa, "Nome", 5)


pessoaFisica = PessoaFisica('111.111.111.1', 'antonio', 29)

print(pessoaFisica.get_idade())
