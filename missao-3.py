# Missão 3: Recuperando o sistema de notas

# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

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