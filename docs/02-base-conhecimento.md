# 📚 Base de Conhecimento

## 📊 Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
| :--- | :--- | :--- |
| `transacoes.csv` | CSV | Analisa padrão de entradas e saídas do cliente e gera resumo de fluxo de caixa. |
| `fluxo_caixa_teste.csv` | CSV | Arquivo de teste para validar o funcionamento do agente em diferentes cenários. |

> [!TIP]
> Para tornar a base mais robusta, você pode incluir históricos de transações mensais ou categorias detalhadas de gastos para criar análises mais completas.

---

## 🛠 Adaptações nos Dados

* **Mock de Dados:** Os dados foram mantidos como simulações de pequenas empresas e microempreendedores.
* **Padronização:** As categorias foram padronizadas para melhor análise (ex.: *Aportes, Vendas de Produtos, Prestação de Serviços, Aluguel, Marketing, Folha Salarial, Software SaaS, Impostos, Logística, Manutenção*).
* **Cenários Adicionais:** Arquivos como `fluxo_caixa_teste.csv` foram criados especificamente para simular diferentes variações de entradas e saídas.

---

## 🧠 Estratégia de Integração

### Como os dados são carregados?
* Todos os CSVs são carregados no início da sessão utilizando a biblioteca **Pandas**.
* No **Streamlit**, o usuário pode enviar seu próprio arquivo (`uploaded_file`), que é processado pela classe `FinancialAnalyzer`.
* Os dados são armazenados em um DataFrame e consolidados em um dicionário de resumo para o Agente.

### Como os dados são usados no prompt?
* **Eficiência de Tokens:** Os dados brutos não são enviados diretamente no *system prompt* da LLM para evitar sobrecarga e limite de tokens.
* **Consulta Dinâmica:** A LLM interpreta a intenção do usuário, e o Agente consulta o resumo determinístico e o DataFrame para gerar respostas precisas.
* **Processamento Prévio:** Perguntas específicas sobre categorias ou valores são tratadas pelo `FinancialAnalyzer` antes de serem enviadas ao usuário.

---

## 📝 Exemplo de Contexto Montado

```text
Resumo do Cliente:
- Total de entradas: R$ 5.000,00
- Total de saídas: R$ 2.488,90
- Saldo final: R$ 2.511,10

Últimas transações:
- 01/10: Salário - Entrada - R$ 5.000,00
- 02/10: Aluguel - Saída - R$ 1.200,00
- 03/10: Supermercado - Saída - R$ 450,00
- 05/10: Netflix - Saída - R$ 55,90
- 07/10: Farmácia - Saída - R$ 89,00
- 10/10: Restaurante - Saída - R$ 120,00
- 12/10: Uber - Saída - R$ 45,00
- 15/10: Conta de Luz - Saída - R$ 180,00
- 20/10: Academia - Saída - R$ 99,00
- 25/10: Combustível - Saída - R$ 250,00

Categoria com maior gasto:
- moradia → R$ 1.380,00 (55,4% do total de despesas)