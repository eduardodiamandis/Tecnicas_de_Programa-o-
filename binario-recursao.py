#transforma um número decimal em binario retornando em string
def binario(n):
    if n < 2:
        return str(n)
    else:
        return binario(n // 2) + str(n % 2)



