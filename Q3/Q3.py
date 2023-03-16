import json  # Importa a biblioteca json para lidar com o arquivo JSON

# Define o nome do arquivo JSON contendo os dados do faturamento diário da distribuidora
json_file_name = 'dados.json'

# Abre o arquivo JSON contendo os dados do faturamento diário da distribuidora
with open(json_file_name, 'r') as json_file:
    # Faz a leitura dos dados do arquivo JSON e converte em um objeto Python
    faturamento = json.load(json_file)

# Inicializa as variáveis de menor e maior faturamento com o primeiro valor diferente de zero
for valor in faturamento:
    if valor['valor'] != 0:
        menor_faturamento = valor['valor']
        maior_faturamento = valor['valor']
        break

# Inicializa as variáveis de soma e contador para cálculo da média mensal
soma_faturamento = 0
contador_faturamento = 0

# Percorre os valores de faturamento diário
for valor in faturamento:
    # Verifica se o valor é maior que o maior valor atual
    if valor['valor'] > maior_faturamento:
        maior_faturamento = valor['valor']
    
    # Verifica se o valor é menor que o menor valor atual e diferente de zero
    if valor['valor'] < menor_faturamento and valor['valor'] != 0:
        menor_faturamento = valor['valor']
    
    # Adiciona o valor do faturamento na soma total e incrementa o contador de faturamentos
    soma_faturamento += valor['valor']
    contador_faturamento += 1

# Calcula a média mensal do faturamento diário
media_faturamento = soma_faturamento / contador_faturamento

# Inicializa o contador de dias em que o valor do faturamento diário foi superior à média mensal
contador_dias_acima_media = 0

# Percorre os valores de faturamento diário
for valor in faturamento:
    # Verifica se o valor é maior que a média mensal
    if valor['valor'] > media_faturamento:
        contador_dias_acima_media += 1

# Imprime os resultados
print('Menor faturamento:', menor_faturamento)
print('Maior faturamento:', maior_faturamento)
print('Dias acima da média:', contador_dias_acima_media)
