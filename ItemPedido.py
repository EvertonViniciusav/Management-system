class ItemPedido:

    def __init__(self,produto, quantidade, observacao, desconto) -> None:
        self.produto=produto
        self.quantidade=quantidade
        self.observacao=observacao
        self.desconto=desconto

    def imprime(self):
        print(
            f"Produto: {self.produto.descricao}\n"
            f"Quantidade: {self.quantidade}\n"
            f"Desconto: {self.desconto}\n"
            f"Observação: {self.observacao}\n"
        )