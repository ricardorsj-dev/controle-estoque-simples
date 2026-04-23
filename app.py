estoque = [] #lista vazia para receber a quantidade de estoque 

#função para entrada dos dados pelo usuário e adição do produto à lista
def adicionar_produto():
    nome = input ("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    minimo = int(input("Digite o estoque mínimo: "))

    produto = {"nome": nome, "preco": preco, "quantidade": quantidade, "minimo": minimo} #dicionario para armazenar os dados do produto
    estoque.append(produto) #funçao append para adicionar o produto na lista 
    print("Produto adicionado com sucesso.\n")

def remover_produto():
    nome = input ("Digite o nome do produto a ser removido: ")
    for produto in estoque:#percorre os produtos na lista estoque para poder remover caso esteja lá 
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print("Produto removido com sucesso.\n")
            return
    print("Produto não encontrado.\n")

def listar_produtos():
    if not estoque:#condiçao para ver se o estoque está vazio 
        print("Estoque vazio.\n")
        return
    
    for produto in estoque: #loop para listar os produtos com seus atributos
        print(f"Nome: {produto['nome']}")
        print(f"Preço: {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")

        if produto["quantidade"] <= produto["minimo"]: #if para definir se o estoque está baixo ou não. Com alerta caso esteja. 
            print(" ⚠️ ESTOQUE BAIXO! ")
        print("=" * 30)

def menu(): #funçao que cria um menu interativo e um while pra controlar o fluxo de cadastros
    while True:
        print("=== CONTROLE DE ESTOQUE ===".center(40))
        print("1 - Adicionar produto")
        print("2- Remover produto")
        print("3 - Listar produtos")
        print("4 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.\n")
            continue

        if opcao == 1:
            adicionar_produto()
        elif opcao == 2:
            remover_produto()
        elif opcao == 3:
            listar_produtos()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

menu()












    




