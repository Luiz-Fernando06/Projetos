import pandas as pd

vendas = {'produto': ['camiseta', 'tenis', 'calça', 'boné'],
             'preço': [50, 200, 120, 40],
             'Quantidade': [10, 5, 8, 15],
             'Categoria': ['Vestuario', 'Calçados', 'Vestuario', 'Acessorios']}
vendas_df = pd.DataFrame(vendas)
#print(vendas_df.head())
categoria_vestuario = vendas_df.loc[vendas_df['Categoria'] == 'Vestuario', ['produto', 'preço', 'Quantidade']]
print('Apenas produtos da categoria vestuario:')
print(categoria_vestuario.to_string(index=False))

produtos_acima_de_100 = vendas_df.query('preço > 100')
print('Apenas produtos acima de 100:')
print(produtos_acima_de_100.to_string(index=False))

vendas_df['Total de vendas'] = vendas_df['preço'] * vendas_df['Quantidade']
print('Visualização de total de vendas:')
print(vendas_df.head().to_string(index=False))

vendas_df['preço'] = vendas_df['preço'].astype(float)
aumentando_10pocent_de_vestuario = vendas_df.loc[vendas_df["Categoria"] == "Vestuario"].copy()
aumentando_10pocent_de_vestuario['preço'] *= 1.1
print('Visualizando preço de vestuario aumentado 10%:')
print(aumentando_10pocent_de_vestuario.to_string(index=False))

ordenando_os_precos_em_decrescente = vendas_df.sort_values(by='preço', ascending=False)
print('Preços ordenandos: ')
print(ordenando_os_precos_em_decrescente.to_string(index=False))

valor_total_de_todos_produtos = vendas_df['Total de vendas'].sum()
print('Valor total de todos os produtos somados: ')
print(valor_total_de_todos_produtos)

produto_caro = vendas_df.loc[vendas_df['preço'].idxmax()]
print('Produto mais caro:')
print(produto_caro.to_string())

produto_barato = vendas_df.loc[vendas_df['preço'].idxmin()]
print('Produto mais barato:')
print(produto_barato.to_string())
