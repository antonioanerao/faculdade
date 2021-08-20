class Contato:
    todos_contatos = []

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

        Contato.todos_contatos.append(self)


class Fornecedor(Contato):
    def pedido(self, pedido):
        print("pedido {} feito por {}", format(pedido, self.nome))


class Amigo(Contato):
    def __init_(self, nome, email, telefone):
        super().__init__(nome, email)
        self.telefone = telefone


contato1 = Contato("Antonio", "blablabla@gmail.com")
fornecedor1 = Fornecedor("nomeFormecedor", "emailFornecedor@aaa.com")

amigo = Amigo("nome", "email")
amigo.telefone = "numero xx"

print(amigo.telefone)
