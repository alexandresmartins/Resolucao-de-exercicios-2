# Função para calcular a sequência de Fibonacci
def fibonacci(n):
    # Inicializa os valores iniciais da sequência
    a, b = 0, 1
    
    # Executa um laço de repetição para calcular a sequência até o n-ésimo termo
    for i in range(n):
        a, b = b, a + b
    
    # Retorna o n-ésimo termo da sequência
    return a

# Recebe a entrada do usuário
numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

# Calcula a sequência de Fibonacci até o número informado
i = 0
encontrou = False
while not encontrou:
    fib = fibonacci(i)
    if fib == numero:
        print(f"{numero} pertence à sequência de Fibonacci.")
        encontrou = True
    elif fib > numero:
        print(f"{numero} não pertence à sequência de Fibonacci.")
        encontrou = True
    else:
        i += 1
