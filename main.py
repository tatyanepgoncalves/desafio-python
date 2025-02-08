# Missão 1 - Restaurando as regras escolares 
def verifica_nota(nota):
  if nota >= 6:
    return "O aluno está aprovado!"
  else:
    return "O aluno está reprovado!"

resultado = verifica_nota(5)
print(resultado)

# Missão 2 - O sistema eleitoral secreto

idade = input("Digite a sua idade: ")

if int(idade) >= 16 :
  print("Você pode votar!")
else:
  print("Você ainda não pode votar!")

# Missão 3: Recuperando o sistema de notas

nota_aluno = input("Qual foi sua nota: ")

if int(nota_aluno) >= 90 and int(nota_aluno) <= 100:
  print("Parabéns, você tirou A")
elif int(nota_aluno) >= 80:
  print("Muito bem, você tirou B")
elif int(nota_aluno) >= 70:
  print("Bom trabalho, você tirou C")
elif int(nota_aluno) >= 60:
  print("Fique atento, você tirou D")
else: 
  print("Estude um pouco mais, você tirou F")

# Missão 4: Restaurando a Identificação de Números 

numero_um = input("Digite um número: ")
numero_dois = input("Digite outro número: ")

soma = int(numero_um) + int(numero_dois)

print("A soma dos números é:", soma)

# Missão 5: Recuperando o Cofre de Segurança 

senha_nova = input("Digite a senha: ")
if senha_nova == "Python123":
  print("Cofre da biblioteca aberto.")
else:
  print("Senha incorreta.")

# Missão 6: Reforçando a Segurança e a Contagem do Sistema

contador = 1

while contador < 11:
  print(contador)
  contador += 1

# Missão 7: Organizando a Lista

lista_numeros = [8, 3, 10, 1, 5]
lista_numeros.sort()
print(lista_numeros)

# Missão 8: Acessando os Registros de Alunos

nome_aluno = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo"]
print(nome_aluno[0])
print(nome_aluno[-1])

# Missão 9: Calculando Dobro de um Número

numero = input("Digite um número: ")

soma = int(numero) + int(numero)

print(f'O dobro de {numero} é', soma)

# Missão 10: Contando Letras
def contar_letras(nome):
  contador = 0
  for letra in nome:
    if letra.isalpha():
      contador += 1
  return contador

nome = input("Digite um nome: ")
quantidade_letras = contar_letras(nome)
print(f'O nome {nome} tem {quantidade_letras} letras.')