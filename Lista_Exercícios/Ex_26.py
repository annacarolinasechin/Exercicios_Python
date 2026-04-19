# exibir dados da classe "Produto" e exibir seus dados: 

class Produto:
    def __init__ (self, nome, valor):
        self.nome = nome
        self.valor = valor

produto1 = Produto("Cintarralho", 200)

print(f"Nome do produto: {produto1.nome};")
print(f"Valor: {produto1.valor}.")