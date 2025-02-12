# Missão 10: Contando Letras

# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

def contar_letras(nome):
  contador = 0
  for letra in nome:
    if letra.isalpha():
      contador += 1
  return contador

nome = input("Digite um nome: ")
quantidade_letras = contar_letras(nome)
print(f'O nome {nome} tem {quantidade_letras} letras.')