texto = input("Digite uma string: ")  # Recebe uma string do usuário
invertido = ""  # Inicializa uma string vazia que será o texto invertido

# Percorre a string de trás para frente, adicionando cada caractere na nova string
for i in range(len(texto)-1, -1, -1):
    invertido += texto[i]

print("String original: ", texto)
print("String invertida: ", invertido)
