class ReportGenerator:

    @staticmethod
    def gerar_relatorio(resumo):
        entradas = resumo["total_entradas"]
        saidas = resumo["total_saidas"]
        saldo = resumo["saldo"]
        categoria, valor_categoria, percentual = resumo["maior_categoria"]


        status = "positivo ✅" if saldo >= 0 else "negativo ⚠️"

        relatorio = f"""
===== RELATÓRIO FINANCEIRO =====

Total de Entradas: R$ {entradas:.2f}
Total de Saídas: R$ {saidas:.2f}
Saldo Final: R$ {saldo:.2f} ({status})

Categoria com maior impacto nas despesas:
- {categoria} → R$ {valor_categoria:.2f} ({percentual:.1f}% do total de gastos)

Análise:
Seu saldo está {status}.
A categoria que mais impacta seu orçamento é '{categoria}'.
Recomenda-se revisar despesas relacionadas a essa categoria para otimizar seu fluxo de caixa.

=================================
"""

        return relatorio
