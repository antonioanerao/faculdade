class Contato:
    todos_contatos = []

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

        Contato.todos_contatos.append(self)

class Fornecedor(Contato):
    def pedido(self,pedido):
        print("AAA")


c=Contato("Fulano", "a@a.com")
f = Fornecedor("FORNECEDOR X", "fornecedor@dd.com")

"""
print(c.nome, c.email, f.nome, f.email)
"""

print(c.todos_contatos)
