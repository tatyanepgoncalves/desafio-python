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