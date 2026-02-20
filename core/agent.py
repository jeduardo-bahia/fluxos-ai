class Agent:
    def __init__(self, resumo, llm_service, analyzer):
        self.resumo = resumo
        self.llm = llm_service
        self.analyzer = analyzer

    def formatar_moeda(self, valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def responder(self, pergunta):

        intencao = self.llm.interpretar_intencao(pergunta)

        if intencao == "saldo":
            return f"Seu saldo atual é {self.formatar_moeda(self.resumo['saldo'])}"

        elif intencao == "maior_entrada":
            dados = (
                self.analyzer.df[self.analyzer.df["tipo"] == "entrada"]
                .groupby("categoria")["valor"]
                .sum()
            )
            categoria = dados.idxmax()
            valor = dados.max()
            return f"A categoria com maior entrada foi '{categoria}', com {self.formatar_moeda(valor)}"

        elif intencao == "maior_saida":
            dados = (
                self.analyzer.df[self.analyzer.df["tipo"] == "saida"]
                .groupby("categoria")["valor"]
                .sum()
            )
            categoria = dados.idxmax()
            valor = dados.max()
            return f"A categoria com maior saída foi '{categoria}', com {self.formatar_moeda(valor)}"

        elif intencao == "menor_saida":
            dados = (
                self.analyzer.df[self.analyzer.df["tipo"] == "saida"]
                .groupby("categoria")["valor"]
                .sum()
            )
            categoria = dados.idxmin()
            valor = dados.min()
            return f"A categoria com menor saída foi '{categoria}', com {self.formatar_moeda(valor)}"

        else:
            return "Pergunte algo como: saldo, maior entrada, maior saída ou menor saída."