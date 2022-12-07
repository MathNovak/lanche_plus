class CaixaEletronico:
   
    def __init__(self, nome):
        self.notas = [100, 50, 20, 10, 5]
        self.nome_banco = nome
 
    def sacar(self, valor_saque):
        resto = -1
        notas = []
        valor = valor_saque
        for valor_nota in self.notas:
            quantidade_notas = valor//valor_nota
            resto = valor% valor_nota
            valor = resto
            if quantidade_notas > 0:
                notas.append(valor_nota)
        if resto == 0:
            self.imprimir_resultado(notas)
        else:
            print('não é possivel sacar')
   
    def imprimir_resultado(self, notas_entregues):
        print(', '.join(notas_entregues))
 
if __name__ == '__main__':
    caixa_eletronico = CaixaEletronico('Ultima Bank')
    valor = int(input('Valor do saque: '))
    caixa_eletronico.sacar(valor)
