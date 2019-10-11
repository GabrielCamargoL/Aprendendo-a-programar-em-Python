#   2) Faça um programa que pegue o nome e as 4 notas de cinco alunos.
#   Calcule a media e o status do aluno.
#   Ao final mostre um boletim da turma com todas suas notas, medias e status.
#   Mostre tambem a media da turma e o numero de aprovados e reprovados.
#-----------------------------------------------------------------------------

somaT= float(0)                                                 # Declaração de variavel 
Aprov= int(0)                                                   # Declaração de variavel
Reprov= int(0)                                                  # Declaração de variavel
Alunos= []                                                      # Declaração de array


for x in range(5):                                              # Repetição para estruturação de dados
    print ("----")                                              # Divisória de alunos
    nome= str(input("Nome: "))                                  # Nome do aluno
    nota1= float(input("1a Nota: "))                            # Nota 1
    nota2= float(input("2a Nota: "))                            # Nota 2
    nota3= float(input("3a Nota: "))                            # Nota 3
    nota4= float(input("4a Nota: "))                            # Nota 4
    media= float((nota1 + nota2 + nota3 + nota4)/4)             # Calculo da media 
    print(f'Media: {media}\n')                                  # Mostrando a media do aluno
    linha= [nome, nota1, nota2, nota3, nota4, media]            # Concatenando informações do aluno em um vetor
    Alunos.append(linha)                                        # Adição das informação em um vetor bidirecional
print ("__" * 9)                                                # Linha dividindo etapas do código
print ("TURMA \n")                                              # Titulo AGENDA



for x in range(len(Alunos)):                                    # Varredura com x= INT para index do vetor
    print (f'Aluno: {Alunos[x][0]}')                            # Apresentação do Nome do aluno
    print (f'1a nota: {Alunos[x][1]}')                          # Apresentação da Nota 1 do aluno
    print (f'2a nota: {Alunos[x][2]}')                          # Apresentação da Nota 2 do aluno
    print (f'3a nota: {Alunos[x][3]}')                          # Apresentação da Nota 3 do aluno
    print (f'4a nota: {Alunos[x][4]}')                          # Apresentação da Nota 4 do aluno
    if Alunos[x][5] >= 7:                                       # Condição se a media do aluno for maior ou igual a 7
        Aprov+=1                                                # Contador de alunos aprovados
        print (f'Media obitida: {Alunos[x][5]} - Aprovado')     # Apresentação da média do aluno e seu Status
        print ("----")                                          # Linha divisória de alunos
    else:                           
        Reprov+=1                                               # Contador de alunos Reprovados
        print (f'Media obitida: {Alunos[x][5]} - Reprovado')    # Apresentação da média do aluno e seu Status
        print ("----")                                          # Linha divisória de alunos



print ("__" * 9)                                                # Linha dividindo etapas do código
print ("MÉDIA GERAL")                                           # Titulo MÉDIA GERAL
print ("----")                                                  # Linha divisória de alunos
for x in range (len(Alunos)):                                   # varredura com x = INT para index do vetor
    somaT= float(somaT + Alunos[x][5])                          # Calculo de soma das medias da turma
    mediaT= float(somaT/len(Alunos))                            # Calculo da media da turma
    
print (f'Média obtida pela Turma: {mediaT}')                    # Média obtida pela turma
print (f'Aprovados: {Aprov}\nReprovados: {Reprov}')             # Contabilização de alunos aprovados e reprovados
print("----")                                                   # Linha divisória de alunos
print ("__" * 9)                                                # Linha Final do código










