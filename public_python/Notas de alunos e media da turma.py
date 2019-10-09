#   2) Faça um programa que pegue o nome e as 4 notas de cinco alunos.
#   Calcule a media e o status do aluno.
#   Ao final mostre um boletim da turma com todas suas notas, medias e status.
#   Mostre tambem a media da turma e o numero de aprovados e reprovados.
#-----------------------------------------------------------------------------

somaT= float(0)
Aprov= int(0)
Reprov= int(0)
Alunos= []
    
for x in range(5):
    nome= str(input("Nome: "))
    nota1= float(input("1a Nota: "))
    nota2= float(input("2a Nota: "))
    nota3= float(input("3a Nota: "))
    nota4= float(input("4a Nota: "))
    media= float((nota1 + nota2 + nota3 + nota4)/4)

    linha= [nome, nota1, nota2, nota3, nota4, media]
    Alunos.append(linha)

print ("__" * 9)
print ("TURMA \n")
print("----")

for x in range(len(Alunos)):
    print (f'Aluno: {Alunos[x][0]}')
    print (f'1a nota: {Alunos[x][1]}')
    print (f'2a nota: {Alunos[x][2]}')
    print (f'3a nota: {Alunos[x][3]}')
    print (f'4a nota: {Alunos[x][4]}')
    if Alunos[x][5] >= 7:
        Aprov+=1
        print (f'Media obitida: {Alunos[x][5]} - Aprovado')
        print ("----")
    else:
        Reprov+=1
        print (f'Media obitida: {Alunos[x][5]} - Reprovado')
        print ("----")
    print ("----")

print ("__" * 9)
print ("MÉDIA GERAL")
print ("----")
for x in range (len(Alunos)):
    somaT= float(somaT + Alunos[x][5])
    mediaT= float(somaT/len(Alunos))

print (f'Média obtida pela Turma: {mediaT}')
print (f'Aprovados: {Aprov}\nReprovados: {Reprov}')
print("----")
print ("__" * 9)










