numError = '\nO número digitado não corresponde a nenhuma das alternativas.\n'
bckMenu = '\nVoltando ao menu...\n'
manutencao = '\nVolte novamente mais tarde, página em manutenção...\n'
traco = '-' * 14


# Listas
# produto: [0]: código, [1]: nome, [2]: fabricante, [3]: preco, [4]: estoque, [5]: quantidade vendida.
produto = []
# cliente: [0]: código, [1]: nome, [3]: cpf.
cliente = []
# admin: [0]: usuário, [1]: senha.
admin = []
# cad: cadastrado.
cadProdutos = []
cadClientes = []
cadAdmin = []


# Funções
def cadastrarProduto():
    # Função chamada para cadastrar um produto.
    escolhaCadastroProduto = int(input('\nDeseja cadastrar um produto?\n1-Sim / 2-Não\n\nEscolha: '))
    if escolhaCadastroProduto == 1:
        cadastraProduto()
    elif escolhaCadastroProduto == 2:
        print(bckMenu)
        gerenciarProdutos()
    else:
        print(numError)
        cadastrarProduto()


def cadastraProduto():
    # Função chamada pela função cadastrarProduto.
    japossui = False
    
    # Recebe o código do produto.
    codP = int(input('\nCódigo para o produto: '))

    # Procurando se o código de produto já foi cadastrado anteriormente:
    for produto in cadProdutos:
        if produto[0] == codP:
            japossui = True
            print('\nCódigo de produto já existente!')
            choose = int(input('1-Tentar novamente / 2-voltar ao menu\n\nEscolha: '))
            if choose == 1:
                # Se o produto já existe, chama novamente a função.
                cadastraProduto()
            elif choose == 2:
                print(bckMenu)
                # Volta ao menu de gerenciamento.
                gerenciarProdutos()
            else:
                # Diz que o número escolhido é inválido e volta ao menu de gerenciamento.
                print(numError,bckMenu)
                gerenciarProdutos()


    # Pedindo informações do produto se ele ainda não tiver sido cadastrado:
    if (not japossui):
        nomeP = str(input('Nome do produto: ').title())
        fabP = str(input('Nome do fabricante: ').title())
        precoP = float(input('Preço do produto: '))
        qntP = int(input('Quantidade em estoque: '))

        vendaP = 0
        # Cadastrando o produto.
        produto = [codP, nomeP, fabP, precoP, qntP, vendaP]
        cadProdutos.append(produto)
        print(f'\nProduto cadastrado!\n\n{traco}\nCód: {produto[0]}\nNome: {produto[1]}\nFabricante: {produto[2]}\nPreço: R${produto[3]:.2f}\nEstoque: {produto[4]}\n{traco}')
        gerenciarProdutos()


def visualizarEstoque():
    # Função para mostrar todos os produtos cadastrados:
    if cadProdutos != []:
        # Se houver produtos cadastrados, mostra-os.
        for produto in cadProdutos:
            print(f'\nCód: {produto[0]}\nNome: {produto[1]}\nFabricante: {produto[2]}\nPreço: R${produto[3]:.2f}\nEstoque: {produto[4]}\n{traco}')
    else:
        print('\nNenhum produto cadastrado')


def alterarPreco():
    # Função para alterar os preços dos produtos:
    passou = False
    if cadProdutos == []:
        # Verifica se existe produto para a troca de preço.
        print('\nNenhum produto cadastrado')
        gerenciarProdutos()
    else:
        # Alterando o preço:
        alterarProduto = int(input('\nCódigo do produto: '))
        for produto in cadProdutos:
            # Verificando a existência do produto:
            if (produto[0] == alterarProduto):
                passou = True
                # Cadastrando novo preço.
                newP = float(input(f'{produto[1]} / {produto[2]}\nValor atual: R${produto[3]:.2f}\nDigite o novo preço: R$'))
                produto[3] = newP
                print('\nPreço alterado com sucesso!')
                gerenciarProdutos()
        if (not passou):
            choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente / 2-voltar ao menu\n\nEscolha: '))
            if choose == 1:
                alterarPreco()
            elif choose == 2:
                print(bckMenu)
                gerenciarProdutos()
            else:
                print(numError,bckMenu)
                gerenciarProdutos()


def vendaProduto():
    # Função para realizar a venda dos produtos:
    passou = False
    if cadProdutos == []:
        print('\nNenhum produto cadastrado')
    else:
        alterarProduto = int(input('\nCódigo do produto: '))
        for produto in cadProdutos:
            if (produto[0] == alterarProduto):
                # Realizando a venda:
                passou = True
                beforeVendaP = produto[5]
                vendaP = int(input(f'Quantidade de {produto[1]} {produto[2]} que deseja vender: '))
                if vendaP <= produto[4]:
                    produto[4] -= vendaP
                    produto[5] = vendaP + beforeVendaP

                    print('\nProduto vendido com sucesso!\n')
                    comprarMais = int(input('Continuar comprando?\n1-Sim / 2-Não\n\nEscolha: '))
                    if comprarMais == 1:
                        vendaProduto()
                    elif comprarMais == 2:
                        print(bckMenu)
                    else:
                        print(numError,bckMenu)
                elif vendaP > produto[4]:
                    print(f'\nEstoque insuficiente!\nEstoque atual de {produto[1]} {produto[2]}: {produto[4]}')
                    print(bckMenu)
        if (not passou):
            choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente / 2-voltar ao menu\n\nEscolha: '))
            if choose == 1:
                vendaProduto()
            elif choose == 2:
                print(bckMenu)
            else:
                print(numError,bckMenu)


def renomearProduto():
    # Função para renomear o produto:
    passou = False
    dentro = False
    if cadProdutos == []:
        print('\nNenhum produto cadastrado')
        gerenciarProdutos()
    else:
        # Perguntando se deseja alterar nome ou fabricante:
        chooseOne = int(input('\nDeseja renomear o produto ou o fabricante?\n1-Produto / 2-Fabricante / 3-Sair\n\nEscolha\n'))
        if chooseOne == 1:
            alterarProduto = int(input('\nCódigo do produto: '))
            for produto in cadProdutos:
                if (produto[0] == alterarProduto):
                    # Realizando a alteração do nome do produto:
                    passou = True
                    newName = str(input(f'Novo nome para {produto[1]} do fabricante {produto[2]}: '))
                    produto[1] = newName
                    print('\nNome alterado com sucesso!')
                    gerenciarProdutos()
        elif chooseOne == 2:
            alterarProduto = int(input('\nCódigo de um produto com o fabricante que deseja renomear: '))
            for produto in cadProdutos:
                if (produto[0] == alterarProduto):
                    # Realizando a alteração do nome do fabricante:
                    passou = True
                    fabForChange = produto[2]
                    allOrOne = int(input(f'Quer alterar {produto[2]}:\n1-Apenas nesse produto / 2-Todos / 3-Sair\n\nEscolha: '))
                    newF = str(input(f'\nNovo nome para {produto[2]}: '))

                    if allOrOne == 1:
                        dentro = True
                        produto[2] = newF
                        print('\nFabricante alterado com sucesso!')
                        gerenciarProdutos()

                    elif allOrOne == 2:
                        for produto in cadProdutos:
                            if produto[2] == fabForChange:
                                dentro = True
                                produto[2] = newF
                                print('\nFabricante alterado com sucesso!')
                        gerenciarProdutos()
                        if (not dentro):
                            print('erro ao renomear')
                            gerenciarProdutos()
                    else:
                        print(numError)
                        gerenciarProdutos()
            if (not passou):
                choose = print('\nProduto não encontrado\n\nTentar novamente-1 / voltar ao menu-2\n\nEscolha: ')
                if choose == 1:
                    renomearProduto()
                elif choose == 2:
                    print(bckMenu)
                    gerenciarProdutos()
                else:
                    print(numError,bckMenu)
                    renomearProduto()
        elif chooseOne == 3:
            print(bckMenu)
            gerenciarProdutos()
        else:
            print(numError)
            renomearProduto()


def removeProduto():
    # Função para remover um produto:
    passou = False
    if cadProdutos == []:
        print('\nNenhum produto cadastrado')
        gerenciarProdutos()
    else:
        removerProduto = int(input('\nCódigo do produto: '))
        for produto in cadProdutos:
            if (produto[0] == removerProduto):
                passou = True
                removerP = int(input(f'\nTem certeza que deseja remover {produto[1]} {produto[2]} do estoque?\n1-Sim / 2-Não\n\nEscolha: '))
                if removerP == 1:
                    # Removendo o produto.
                    cadProdutos.remove(produto)
                    print('\nProduto removido do estoque!')
                    print(bckMenu)
                    gerenciarProdutos()
                else:
                    print(numError,bckMenu)
                    gerenciarProdutos()

        if (not passou):
            choose = int(input('\nProduto não encontrado\n\n1-Tentar novamente / 2-voltar ao menu\n\nEscolha: '))
            if choose == 1:
                removeProduto()
            elif choose == 2:
                print(bckMenu)
                gerenciarProdutos()
            else:
                print(numError,bckMenu)
                gerenciarProdutos()


def mostrarVendas():
    # Função para mostrar as vendas realizadas de cada produto:
    venda = False
    if cadProdutos == []:
        print('\nNenhum produto cadastrado')
        print(bckMenu)
        gerenciarProdutos()
    else:
        for produto in cadProdutos:
            if produto[5] != 0:
                venda = True
                print(f'\nCód: {produto[0]} / Nome: {produto[1]}\nFabricante: {produto[2]}\nPreço: R${produto[3]:.2f}\nProdutos vendidos: {produto[5]}\nEstoque restante: {produto[4]}\n{traco}')
        if (not venda):
            print('\nVenda produtos para visualizar esta página!')
    gerenciarProdutos()


def cadastrarCliente():
    # Função para cadastrar novos clientes:
    japossui = False
    escolhaCadastroCliente = int(input('\nDeseja cadastrar um cliente?\n1-Sim / 2-Não\n\nEscolha: '))
    if escolhaCadastroCliente == 1:
        cadastraCliente()
    elif escolhaCadastroCliente == 2:
        print(bckMenu)
    else:
        print(numError)
        cadastrarCliente()


def cadastraCliente():
    # Função chamada pela função cadastrarCliente.
    japossui = False
    passou = False
    codC = int(input('\nCódigo para o cliente: '))

    for cliente in cadClientes:
        if cliente[0] == codC:
            print('\nCódigo de cliente já existente!')
            japossui = True
            cadastraCliente()

    if (not japossui):
        nomeC = str(input('Nome do cliente: ').title())
        cCpf = int(input('Deseja cadastrar CPF?\n1-Sim / 2-Não\n\nEscolha: '))
        if cCpf == 1:
            passou = True
            print('\n(digite apenas números)\n')
            cpfC = input('CPF do cliente: ')
        if (not passou):
            cpfC = 0

        cliente = [codC, nomeC, cpfC]
        cadClientes.append(cliente)
        print('\nCliente cadastrado!\n')
        if cpfC != 0:
            print(f'{traco}\nCód: {cliente[0]}\nSr(a): {cliente[1]}\nCPF: {cliente[2]}\n{traco}')
        else:
            print(f'{traco}\nCód: {cliente[0]}\nSr(a): {cliente[1]}\nCPF: Não cadastrado!\n{traco}')


def visualizarClientes():
    # Função para visualizar os clientes cadastrados:
    if cadClientes == []:
        print('\nNenhum cliente cadastrado')
    else:
        for cliente in cadClientes:
            if cliente[2] == 0:
                print(f'\nCód: {cliente[0]}\nSr(a): {cliente[1]}\nCPF: Não cadastrado!\n{traco}')
            else:
                print(f'\nCód: {cliente[0]}\nSr(a): {cliente[1]}\nCPF: {cliente[2]}\n{traco}')


def lucro():
    nome = str(input('\nNome do produto: '))
    qnt = int(input('Quantidade comprada: '))
    pagoP = float(input('Preço total pago: R$'))
    porcentagem = int(input('Qual será a porcentagem de lucro?\n'))

    pago = pagoP / qnt
    porcentagemD = porcentagem / 100
    totalPorcentagem = pago * porcentagemD
    total = pago + totalPorcentagem
    
    print(f'Ao vender {nome} com {porcentagem}% de lucro, equivalente a R${totalPorcentagem:.2f} por produto vendido com o valor de R${total:.2f}')
    print(bckMenu)


def verificaGerenciar():
    # Função para verificar:
    passouLogin = False
    passouSenha = False
    login = str(input('\nLogin: '))
    senha = str(input('Senha: '))

    for admin in cadAdmin:
        if admin [0] == login:
            passouLogin = True
            if admin[1] == senha:
                passouSenha = True
                gerenciarProdutos()
    if (not passouLogin and not passouSenha):
        print('\nLogin e senha inválidas')
    if (passouLogin == True and not passouSenha):
        print('\nSenha inválida')


def cadastrarAdmin():
    # Função para cadastrar um admnistrador do sistema:
    japossui = False
    print('\nCadastrando administrador!\n')
    adminL = input('\nDigite o nome de usuário de administrador: ')
    if cadAdmin == []:
        adminS = input('Digite uma senha: ')
        admin = [adminL,adminS]
        cadAdmin.append(admin)
        print('\nAdministrador cadastrado!')
    else:
        for admin in cadAdmin:
            if adminL == admin[0]:
                japossui = True
                print('\nUsuário já existente!')
                gerenciarProdutos()
        if (not japossui):
            adminS = str(input('Digite uma senha: '))
            admin = [adminL,adminS]
            cadAdmin.append(admin)
            print('\nAdministrador cadastrado!')
            gerenciarProdutos()


def visualizarAdmin():
    if cadAdmin != []:
        for admin in cadAdmin:
            print(f'\nLogin: {admin[0]}\nSenha: {admin[1]}\n{traco}')
    gerenciarProdutos()


def removerAdmin():
    # Função para remoção de um administrador do sistema:
    passou = False
    if cadAdmin == []:
        print('\nNenhum administrador cadastrado')
        cadastrarAdmin()
    else:
        if len(cadAdmin) > 1:
            removerAdmin = input('\nLogin do administrador para a remoção: ')
            for admin in cadAdmin:
                if removerAdmin == admin[0]:
                    passou = True
                    removerA = int(input(f'\nTem certeza que deseja remover\n\n{traco}\nLogin: {admin[0]}\nSenha: {admin[1]}\n{traco}\n\n1-Sim / 2-Não\n\nEscolha: '))
                    if removerA == 1:
                        cadAdmin.remove(admin)
                        print('\nAdministrador removido do estoque!')
                        print(bckMenu)
                        gerenciarProdutos()
                    else:
                        print(numError,bckMenu)
                        gerenciarProdutos()
        else:
            print('\nExiste apenas um administrador!')
            passou = True
            gerenciarProdutos()
        if (not passou):
            choose = int(input('\nAdministrador não encontrado\n\n1-Tentar novamente / 2-voltar ao menu\n\nEscolha: '))
            if choose == 1:
                removerAdmin()
            elif choose == 2:
                print(bckMenu)
                gerenciarProdutos()
            else:
                print(numError,bckMenu)
                gerenciarProdutos()


def administrarAdmin():
    # Função para administrar os administradores do sistema:
    print('\nSistema De Mercado\n||' + '=' * 15 + '||\n||  Bem-Vindo(a) ||\n||' + '=' * 15 + '||\n')
    admMenu = int(input('1-Cadastrar novo administrador\n2-Ver administradores\n3-Remover um administrador\n0-Voltar ao menu de gerenciamento\n\nEscolha: '))
    if admMenu > 3 or admMenu < 0:
        print(numError)
        administrarAdmin()
    elif admMenu == 1:
        cadastrarAdmin()
    elif admMenu == 2:
        visualizarAdmin()
    elif admMenu == 3:
        removerAdmin()


def gerenciarProdutos():
    # Menu de gerenciamento:
    print('\nSistema De Mercado\n||' + '=' * 15 + '||\n||  Bem-Vindo(a) ||\n||' + '=' * 15 + '||\n')
    mngMenu = int(input('1-Cadastrar produto\n2-Alterar preço\n3-Renomear produto ou fabricante\n4-Remover produto\n5-Lista de vendas\n6-Cadastrar cliente\n7-Visualizar clientes\n9-Gerenciar Administradores\n0-Voltar ao menu principal\n\nEscolha: '))
    if mngMenu > 9 or mngMenu < 0 or mngMenu == 8:
        print(numError)
        gerenciarProdutos()
    elif mngMenu == 1:
        cadastrarProduto()
    elif mngMenu == 2:
        alterarPreco()
    elif mngMenu == 3:
        renomearProduto()
    elif mngMenu == 4:
        removeProduto()
    elif mngMenu == 5:
        mostrarVendas()
    elif mngMenu == 6:
        cadastrarCliente()
    elif mngMenu == 7:
        visualizarClientes()
    elif mngMenu == 9:
        administrarAdmin()
    elif mngMenu == 0:
        print(bckMenu)


def maisMenu():
    # Menu com algumas funções extras:
    print('\nSistema De Mercado\n')
    print("||" + "=" * 15 + "||\n||  Bem-Vindo(a) ||\n||" + "=" * 15 + "||\n")
    moreMenu = '1-Calcular lucro\n0-Voltar ao menu principal\n\nEscolha: '

    moreMenu = int(input(moreMenu))

    if moreMenu < 0 or moreMenu > 1:
        print(numError)
        maisMenu()
    elif moreMenu == 1:
        lucro()
    elif moreMenu == 0:
        print(bckMenu)


#Início da execução
sair = False
while (not sair):
    # Menu Principal
    if cadAdmin == []:
        cadastrarAdmin()
    print('\nSistema De Mercado\n||' + '=' * 15 + '||\n||  Bem-Vindo(a) ||\n||' + '=' * 15 + '||\n')
    mainMenu = '1-Visualizar estoque\n2-Vender produto\n3-Gerenciar\n4-Mais opções\n0-Sair\n\nEscolha: '

    opcao = int(input(mainMenu))

    if opcao < 0 or opcao > 5:
        print(numError)
    elif opcao == 1:
        visualizarEstoque()
    elif opcao == 2:
        vendaProduto()
    elif opcao == 3:
        verificaGerenciar()
    elif opcao == 4:
        maisMenu()
    elif opcao == 0:
        sai = int(input('\nDeseja encerrar o sistema?\n1-Sim / 2-Não\n\nEscolha: '))
        if sai == 1:
            print('\nSaindo...')
            sair = True
        elif sai == 2:
            print(bckMenu)
        else:
            print(numError,bckMenu)
