import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def gerar_fluxo_caixa(n_transacoes=1000):
    # Configurações de Categorias
    categorias_receita = ['Vendas de Produtos', 'Prestação de Serviços', 'Rendimentos', 'Aportes']
    categorias_despesa = ['Aluguel', 'Marketing', 'Folha Salarial', 'Software SaaS', 'Impostos', 'Logística', 'Manutenção']
    
    dados = []
    data_inicial = datetime(2025, 1, 1)

    for i in range(n_transacoes):
        # 1. Define se é Entrada ou Saída (60% saídas para testar análise de risco)
        tipo = np.random.choice(['entrada', 'saida'], p=[0.4, 0.6])
        
        # 2. Escolhe categoria e define valor
        if tipo == 'entrada':
            categoria = random.choice(categorias_receita)
            valor = round(random.uniform(1000, 15000), 2) # Entradas maiores
        else:
            categoria = random.choice(categorias_despesa)
            valor = round(random.uniform(50, 4500), 2) # Despesas pulverizadas
            
        # 3. Gera data aleatória ao longo do ano
        data_transacao = data_inicial + timedelta(days=random.randint(0, 365))
        
        dados.append({
            'ID': i + 1,
            'data': data_transacao.strftime('%Y-%m-%d'),
            'tipo': tipo,
            'categoria': categoria,
            'valor': valor,
            'descricao': f"Transação referente a {categoria}"
        })

    # Criar DataFrame e ordenar por data
    df = pd.DataFrame(dados)
    df = df.sort_values(by='data')
    
    # Salvar CSV
    df.to_csv('fluxo_caixa_teste.csv', index=False, encoding='utf-8')
    return df

# Executar
df_teste = gerar_fluxo_caixa(1500) # Gerando 1.500 linhas
print("✅ Arquivo 'fluxo_caixa_teste.csv' gerado com 1500 linhas!")
print(df_teste.head())