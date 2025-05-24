n = input('Digite um número para calcular o fatorial: ')
def fatorial(n):
  if n >= 0:
    result = 1
    for i in range(1,n+1):
    # for i in range(2,n+1):
      # result = result * i
      result *= i
    return result
  else:
    return 'O número deve ser positivo'
resultado = fatorial(int(n))
print(f"O fatorial de {n} é {resultado}")
