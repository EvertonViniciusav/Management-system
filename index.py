from Produto import Produto
from Cliente import Cliente
from Pedido import Pedido
from ItemPedido import ItemPedido
from datetime import datetime

listaProdutos = [] 
listaClientes = []
listaPedidos = []
listaItens = []

def buscarProduto(buscaCod):
    i = 0
    for objetoBusca in listaProdutos:
        if objetoBusca.cod==buscaCod:
            return objetoBusca, i
        i+=1
    return None, i

def buscarCliente(buscaCPF):
    i = 0
    for objetoBusca in listaClientes:
        if objetoBusca.cpf==buscaCPF:
            return objetoBusca, i
        i+=1
    return None, i

def menuProdutos():
    while(True):
        print("\n\nBEM VINDO AO SISTEMA DE PRODUTOS")
        print("Escolha uma opção: \n"
            "1 - 💾 Cadastrar Produto\n"
            "2 - 🔎 Listar Produtos\n"
            "3 - ✏️ Alterar Produto\n"
            "4 - ❌ Excluir Produto\n"
            "0 - ⬅️ Voltar ")
        escolha = input("Digite:")

        if escolha=="0":
            break
        

        elif escolha=="1":
            print("\n\n💾 CADASTRO DE PRODUTOS:")
        
            codigo=input("Código do Produto:")
            descricao=input("Descrição do Produto:")
            preco=float(input("Preço R$:"))
            qtd=int(input("Quantidade em Estoque:"))

            objetoProduto = Produto(codigo,descricao, preco, qtd)
            listaProdutos.append(objetoProduto)


        elif escolha=="2":
            print("\n\n🔎 LISTA DE PRODUTOS CADASTRADOS:")
            for produto in listaProdutos:
                produto.listar()


        elif escolha=="3":
            print("\n\n✏️ ALTERAR INFORMAÇÕES SOBRE UM PRODUTO:")
            codigo =  input("Informe o Codigo do Produto:")
        
            produto, posicao = buscarProduto(codigo)
            if produto is None:
                print("Produto Não encontrado!")
            else:
                descricao=input("Descrição do Produto:")
                preco=float(input("Preço R$:"))
                qtd=int(input("Quantidade em Estoque:"))
                produto.alterar(descricao, preco, qtd)

                listaProdutos[posicao]=produto

                print("Produto excluído com sucesso!")


        elif escolha=="4":
            print("\n\n❌ EXCLUIR PRODUTO:")
            codigo =  input("Informe o Codigo do Produto:")
        
            produto, posicao = buscarProduto(codigo)
            if produto is None:
                print("Produto Não encontrado!")
            else:
                listaProdutos.pop(posicao)
                print("Produto Excluído com Sucesso!")


        else:
            print("Opção Inválida!")

def menuClientes():
    while(True):
        print("\n\n 👤BEM VINDO AO SISTEMA DE CLIENTES")
        print("Escolha uma opção: \n"
            "1 - 💾 Cadastrar Cliente\n"
            "2 - 🔎 Listar Cliente\n"
            "3 - ✏️ Alterar Cliente\n"
            "0 - ⬅️ Voltar ")
        escolha = input("Digite:")

        if escolha=="0":
            break

        elif escolha=="1":
            print("\n\n💾 CADASTRO DE CLIENTE:")
        
            cpf=input("CPF:")
            nome=input("Nome Cliente:")
            telefone=input("Telefone:")
            endereco=input("Endereço:")

            objetoCliente = Cliente(cpf=cpf, endereco=endereco, telefone=telefone, nome=nome)
            listaClientes.append(objetoCliente)

        elif escolha=="2":
            print("\n\n🔎 LISTA DE CLIENTES CADASTRADOS:")
            for objetoCliente in listaClientes:
                objetoCliente.imprimir()

        elif escolha=="3":
            print("\n\n✏️ ALTERAR INFORMAÇÕES SOBRE UM CLIENTE:")
            cpf =  input("Informe o CPF do cliente:")
        
            cliente, posicao = buscarCliente(cpf)
            if cliente is None:
                print("Cliente Não encontrado!")
            else:
                nome=input("Nome Cliente:")
                telefone=input("Telefone:")
                endereco=input("Endereço:")
                cliente.alterar(nome, telefone, endereco)

                listaClientes[posicao]=cliente

                print("Produto excluído com sucesso!")

        else:
            print("Opção Inválida!")

while(True):
    print("\n\n BEM VINDO AO SISTEMA DE LANCHONETE")
    print("Escolha uma opção: \n"
        "1 - 👤 Clientes \n"
        "2 - 📦 Produtos \n"
        "3 - 🛒 Novo Pedido \n"
        "0 - ⬅️ Sair ")
    escolha = input("Digite:")

    if escolha=="0":
        break

    elif escolha=="1":
        menuClientes()

    elif escolha=="2":
        menuProdutos()

    elif escolha=="3":
        while(True):
            print("\n\n BEM VINDO AO SISTEMA DE ITEM DO PEDIDO")
            print("Escolha uma opção: \n"
                "1 - 🛒 Novo Item \n"
                "0 - ⬅️ Sair ")
            escolha = input("Digite:")

            if escolha=="0":
                break

            else:
                tempo = str(datetime.today())
                data = tempo[0:10]
                hora = tempo[11:16]
                cpf = input("Digite o CPF do Cliente: ")
                objetoCliente, posicao = buscarCliente(cpf)
                if(objetoCliente is None):
                    print("Cliente Não Encontrado!")
                else:
                    print(f"Cliente ", objetoCliente.nome)
                    pagamento = input("Informe a forma de pagamento: ")
                    pedidoNum = len(listaPedidos)+1
                    codigoProduto = input("Informe o Codigo do Produto: ")
                    objetoProduto, i = buscarProduto(codigoProduto)
                    if(objetoProduto is None):
                        print("Produto Não encontrado!")
                    else:
                        quantidade = input("Informe a  Quantidade: ")
                        observacao = input("Informe a  Observação: ")
                        desconto = float(input("Informe o Desconto: "))
                        objetoItensPedido = ItemPedido(objetoProduto, quantidade, observacao, desconto)
                        listaItens.append(objetoItensPedido)
                        objetoPedido = Pedido(pedidoNum, data, hora, pagamento, objetoCliente, listaItens)
                        objetoPedido.imprimir()
                        listaPedidos.append(objetoPedido)

    else:
         print("Opção Inválida!")

print("\n bye! ( >‿◠ ) ✌")