'''
    Estudo sobre list comprehension
    
    O que é?
        São expressões compactas que podem criar uma lista de forma mais eficiente    
    
    Quando usar?
        - Criar uma lista a partir de outra lista
        - Filtrar elementos por uma condição
        - Usar uma forma compacta e legível para lidar com listas
        - Combinar os elementos de vários iteráveis usando uma lógica
        - Quando a lógica interna for simples e clara, sem muitas estruturas de repetição ou condicionais
    Formato:
        - Mapeamento simples
            [expressao for item iteravel]
        - Filtro
            [expressao for item iteravel condicao]       
        - Filtro e else
            [expresao condicao else for item iteravel]
        - Multiplos fors
            [expressao for item iteravel for item iteravel]
        - Fors e condicoes
            [expressao for item iteravel for item iteravel condicao ]
        - Fors aninhados e condicaoes
            [expressao for item [expressao for item iteravel condicao] condicao]
    Exceções
        Não há: break, continue ou return em list comprehension 
'''     


# Criando nova lista a partir da compreesão

## Criando uma lista de números primos de 0 até 100

### For
numeros = list(range(0,101))

primos = list()
for numero in numeros:
    if numero >=2:
        for nu in range(2, numero+1):
            if numero%nu == 0 and nu!=numero:
                break
            elif numero == nu:
                primos.append(numero)
print(primos)

### List comprehension
numeros = list(range(0,101))
primos = [primo for primo in [numero for numero in numeros if len([divisor for divisor in range(2, numero+1) if numero%divisor == 0]) == 1]]
print(primos)




