# Missão 2 - O sistema eleitoral secreto

# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = input("Digite a sua idade: ")

if int(idade) >= 16 :
  print("Você pode votar!")
else:
  print("Você ainda não pode votar!")
