class ArquivoAAC:
    def __init__(self, arquivo):
        if not arquivo.endswith(".acc"):
            raise Exception("Formato inválido")
        self.arquivo = arquivo


    def tocar(self):
        print("Tocando {} como aac".format(self.arquivo))

aac = ArquivoAAC('aaa.acc')

aac.tocar()