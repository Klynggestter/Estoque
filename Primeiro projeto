# Definindo estruturas de dados
produtos = []  # Array para produtos
movimentacoes = []  # Array para as movimentações

# Cadastrar Produtos
def cadastrar_produto(id_produto, nome, categoria, quantidade, preco, localizacao):
    # Verifica se o produto ja existe
    for produto in produtos:
        if produto['id_produto'] == id_produto:
            print(f"Produto com ID {id_produto} já cadastrado.")
            return

    # Variável que armazena os dados do produto
    novo_produto = {
        'id_produto': id_produto,
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco,
        'localizacao': localizacao
    }

    # Usando a função append para adicionar o novo produto
    produtos.append(novo_produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

# Consultar Produto
def consultar_produto(id_produto):
    for produto in produtos:
        if produto['id_produto'] == id_produto:
            print(f"Produto Encontrado: {produto}")
            return produto
    print(f"Produto com ID {id_produto} não encontrado.")
    return None

# Registrar Movimentação
def registrar_movimentacao(id_produto, tipo_movimentacao, quantidade, data_movimentacao):
    produto = consultar_produto(id_produto)

    if produto is None:
        print("Movimentação não pode ser registrada: Produto não encontrado.")
        return

    if tipo_movimentacao == "entrada":
        produto['quantidade'] += quantidade
    elif tipo_movimentacao == "saida":
        if produto['quantidade'] < quantidade:
            print("Quantidade insuficiente para a saída.")
            return
        produto['quantidade'] -= quantidade
    else:
        print("Tipo de movimentação inválido. Use 'entrada' ou 'saida'.")
        return

    # Registrar a movimentação
    movimentacao = {
        'id_produto': id_produto,
        'tipo': tipo_movimentacao,
        'quantidade': quantidade,
        'data': data_movimentacao
    }

    movimentacoes.append(movimentacao)
    print(f"Movimentação de {tipo_movimentacao} registrada com sucesso.")

# Gerar Relatorio
def gerar_relatorio_produtos():
    print("\nRelatório de Produtos:")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"ID: {produto['id_produto']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']},"
            f" Preço: {produto['preco']}, Localização: {produto['localizacao']}")

# Historico Movimentacao
def consultar_historico_movimentacoes():
    print("\nHistórico de Movimentações:")
    if not movimentacoes:
        print("Nenhuma movimentação registrada.")
        return

    for mov in movimentacoes:
        print(
            f"Produto ID: {mov['id_produto']}, Tipo: {mov['tipo']}, Quantidade: {mov['quantidade']}, Data: {mov['data']}")


# Usando as funções
# Cadastrar produtos
cadastrar_produto(1, 'mouse', 'informatica', 15, 1.700, 'Corredor l')
cadastrar_produto(2, 'Calça GG', 'Roupa', 25, 135, 'corredor 5')

# Registrar movimentações
registrar_movimentacao(1, 'entrada', 20, '25.09.2014')
registrar_movimentacao(2, 'saida', 5,'15.09.2024')

# Gerar relatórios
gerar_relatorio_produtos()
consultar_historico_movimentacoes()
