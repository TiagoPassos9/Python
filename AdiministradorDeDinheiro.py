value = []
values = []

def showValues():
    if values != []:
        for produto in values:
            print(f'\nNome: {produto[0]}\nPreço: R${produto[1]:.2f}  ||  Parcela atual: {produto[2]} de {produto[3]}')
            if produto[3] > 1:
                parcelaMensal = produto[1] / produto[3]
                print(f'Parcela Mensal: R${parcelaMensal:.2f}')
        lastTotal = 0.0
        total = 0.0
        for produto in values:
            if produto[3] == 1:
                total = lastTotal + produto[1]
            else:
                parcelaMensal = produto[1] / produto[3]
                total = lastTotal + parcelaMensal
            lastTotal = total
        print(f'\nValor total a pagar desse mês: {total:.2f}'.replace('-',''))
        soma = salario-total
        if soma > 0:
            print(f'Sobra: {soma:.2f}')
        elif soma < 0:
            print(f'Falta {soma:.2f}'.replace('-',''))
    else:
        print('\nNenhum produto cadastrado')


def addValue():
    name = input('nome: ')
    add = float(input('valor: ').replace(',','.'))
    parcelaAtual = 1
    parcelas = int(input('Número de parcelas: '))

    if parcelas == 0:
        parcelas = 1

    value = [name, add, parcelaAtual, parcelas]
    values.append(value)


def removeValue():
    name = input('nome do produto cadastrado: ')
    for produto in values:
        if produto[0] == name:
            print(f'\nNome: {produto[0]}\nPreço: R${produto[1]:.2f}  ||  Parcela atual: {produto[2]} de {produto[3]}')
            confirma = int(input('Deseja remover esse produto? (1 - sim, 2 - não)\n\nResposta: '))
            if confirma == 1:
                values.remove(produto)


salario = float(input('salario: '))
sair = False
while (not sair):

    print('\nAdministrador de dinheiro\n||' + '=' * 15 + '||\n||  Bem-Vindo(a) ||\n||' + '=' * 15 + '||\n')
    mainMenu = '1-Visualizar valores\n2-Adicionar valor\n3-Remover valor\n4-Sair\n\nEscolha: '

    opcao = int(input(mainMenu))

    if opcao < 0 or opcao > 4:
        print('Número inválido')
    elif opcao == 1:
        showValues()
    elif opcao == 2:
        addValue()
    elif opcao == 3:
        removeValue()
    elif opcao == 4:
        print('Obrigado por utilizar o sistema <3')
        sair = True
    else:
        print('Número inválido')
