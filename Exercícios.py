#Questão 1
def produto(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

n= int(input("Digite um número:"))
print(f"\nResultado: {produto(n)}")

#Questão 2
def imprime_intervalo(inicio, fim):
    for i in range(inicio, fim + 1):
        print(i)

inicio = int(input("\nInforme o início do intervalo: "))
fim = int(input("\nInforme o fim do intervalo: "))
imprime_intervalo(inicio, fim)

#Questão 3
def potencia(x, n):
    resultado = 1
    for i in range(abs(n)):
        resultado *= x
    if n < 0:
        return 1 / resultado
    else:
        return resultado

x= int(input("\nDigite o valor da base:"))
n=int(input("\nDigite o valor que será elevado:"))

print(f"\nResultado: {potencia(x,n)}")

#Questão 4
def s():
    soma = 0
    for n in range(1, 51):
        termo = (2*n - 1) / n
        print(f"{2*n - 1}/{n} + ", end="")
        soma += termo
    print(f"\nO valor de S é: {soma:.2f}")

s()

#Questão 5
def sucessor(n):
    return n + 1

def predecessor(n):
    return n - 1

def calcula_soma(x, y):
    if y == 0:
        return x
    else:
        return sucessor(calcula_soma(x, predecessor(y)))
    
x = int(input("\nDigite um número:"))
y = int(input("\nDigite um número:"))
resultado = calcula_soma(x, y)
print(f"\nA soma de {x} e {y} é: {resultado}")  

#Questão 6
def busca_binaria(vet, v):
    inf = 0
    sup = len(vet) - 1

    while inf <= sup:
        meio = (inf + sup) // 2

        if vet[meio] == v:
            return meio  

        elif vet[meio] < v:
            inf = meio + 1

        else:
            sup = meio - 1

    return False  

vet=[]
for n in range(0, 10+1):
    x=int(input("\nDigite um número:"))
    vet.append(x)
print(vet)
v =int(input("\nDigite a posição que quer acessar:"))

resultado = busca_binaria(vet, v)

if resultado is not False:
    print(f"Valor {v} encontrado na posição {resultado}")
else:
    print(f"Valor {v} não encontrado")

#Questão 7
def binario(x):
    if x == 0:
        return '0'
    elif x == 1:
        return '1'
    else:
        return binario(x // 2) + str(x % 2)
    
x =int(input("\n Digite o número que deseja converter para binário:"))
print(f"\nResultado da Conversão:{binario(x)}")  
