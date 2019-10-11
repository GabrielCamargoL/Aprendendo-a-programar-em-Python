#   1) Faça um programa de Agenda usando Lista bidimensional.
#      O programa deve ter um menu que permita:
#           
#           1- Cadastrar
#           2- Consultar
#           3- Mostrar todos contatos
#           4- Sair
#-------------------------------------------------------------------------
#   2) Inclua o cadastro do telefone em um mesmo array.
#-------------------------------------------------------------------------
#   3) Na opção Consulta ofereça as opçoes alterar e excluir. Use a função
#      Remove para excluir |("lista.remove ('item da lista')|
#                          |  lista.pop(index)              |
#                          |  del lista[index]              |
#-------------------------------------------------------------------------

Contatos= []                                                # Declaração de vetor
x= str('')                                                  # Declaração de variavel
while True:                                                 # Criando um Looping com possibilidade de finaçização do programa
    
    print (18* "__")                                        # Linha para dividir etapas do programa
    print ()                                                # Quebra de linha para melhor visualização
    
    print ("1) Cadastrar.")                                 # Opções para o usuário
    print ("2) Consultar.")                                 # Opções para o usuário
    print ("3) Mostrar todos os contatos")                  # Opções para o usuário
    print ("4) Sair")                                       # Opções para o usuário

    print ()                                                # Quebra de linha para melhor visualização

    opcao= int(input("Digite uma opcao para avançar: "))    # Opções para o usuário

#--------------------------------------------------------------------------

    if opcao == 1:                          # Opção Cadastrar Contato
        nome =str(input("Nome: ")).lower()  # Nome do Contato
        tel = str(input("Tel: "))           # Telefone do Contato
        
        linha= [nome,tel]                   # Concatenação das informações em um vetor
        Contatos.append(linha)              # Adição do vetor dentro da lista Contatos (Vetor bidimensional)
        
#--------------------------------------------------------------------------

    elif opcao == 2:                                                        # Opção Consultar contato                                      
        Consulta= str(input("Digite o nome do contato: ")).lower()          # Pesquisa do Usuário ("lower" para nao haver incompatibilidade com letras maiusculas e minusculas)
        for i in range(len(Contatos)):                                      # varredura em INT para index do array
            if(i >= len(Contatos)):                                         # Condição de variável i for maior o comprimento do array (out of range)
                break		                                                # Evitando erro de out of range in "i"
            
            for z in (Contatos[i]):                                         # Varredura de string (nome) para comparação da condição seguinte
                #print (z)  <-- teste de comportamento
                if z == Consulta:                                           # Condição de nome pesquisado = nome na lista Contatos
                    print (f'Nome: {Contatos[i][0]}')                       # Se Condição verdadeira, Mostrar nome pesquisado
                    print (f'Tel: {Contatos[i][1]}')                        # Se Condição verdadeira, Mostrar Telefone pesquisado
                    print ()                                                # Quebra de linha
                        
                    print ("1) Alterar dados do Contato.")                  # Opções do menu de alteração da lista Contatos
                    print ("2) Excluir contato.")                           # Opções do menu de alteração da lista Contatos
                    print ("3) Voltar ao inicio.")                          # Opções do menu de alteração da lista Contatos
                                
                    opcao2= int(input("Digite uma opção para continuar: ")) # Seleciona uma opçao acima desta instrução
                    while opcao2!=1 and opcao2!=2 and opcao2!=3:  	        # Opção inexistente das que estavam disponíveis (menu de alteração)
                        print("Opção inexistente!")                         # Mensagem de Opcao inválida
                        opcao2= int(input("Digite a opção novamente: "))    # Solicita ao usuário para digitar novamente

                    if (opcao2 == 1):                                       # Opção Alterar dados do Contato
                        Contatos[i][0]= str(input("Nome: ")).lower()        # Alteração do Nome previamente soliciado
                        Contatos[i][1]= str(input("Tel: "))                 # Alteração do Telefone previamente solicitado
                        
                    elif (opcao2 == 2):                                     # Opção Remover contato
                        Contatos.pop(i)                                     # Remoção do Contato e seu respectivo telefone (i = linha do vetor)
                        break                                               # "Break" para quebrar a rotina de varredura "for" e evitar o erro "out of range"

                    elif (opcao2 == 3):		                                # Opção retornar para o menu
                        print ("Voltando ao inicio...")                     # Mensagem de retorno
                 
#--------------------------------------------------------------------------
                    
    elif opcao == 3:                            # Mostrar todos os Contatos
        print ("__"* 18,"\n")                   # Traço para dividir etapas
        print ("AGENDA")                        # Titulo AGENDA
        print ("----")
        for x in range(len(Contatos)):          # Varredura na lista Contatos.
            print (f'Contato {x+1}:')           # Contato de numero (1,2,...,N)   x+1 para não ter "Contato 0"
            print (f'Nome: {Contatos[x][0]}')   # Nome: celula de linha variavel e coluna constante no vetor
            print (f'Tel: {Contatos[x][1]}')    # Tel: celula de linha variavel e coluna constante no vetor
            print ("----")                      # Divisória de Contatos

#--------------------------------------------------------------------------

    elif opcao == 4:    # Sair do Programa
        break           # Interrompe o Loop while True (loop infinito do código)

#-------------------------------------------------------------------------
    
    else:
        print("Opção inexistente!")     # Opção diferente das que estavam disponíveis (menu de seleção)
                
                
            
    

    
    
