#   1) Faça um programa de Agenda usando Lista.
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

Contatos= []
x= str('')
while True:
    
    print (18* "__")     # Quebra de linha para melhor visualização :)
    print ()             #
    
    print ("1) Cadastrar.")
    print ("2) Consultar.")
    print ("3) Mostrar todos os contatos")
    print ("4) Sair")

    print ()

    opcao= int(input("Digite uma opcao para avançar: "))

#--------------------------------------------------------------------------

    if opcao == 1:
        nome =str(input("Nome: ")).lower()
        tel = str(input("Tel: "))
        
        linha= [nome,tel]
        Contatos.append(linha)
        
#--------------------------------------------------------------------------

    elif opcao == 2:
        Consulta= str(input("Digite o nome do contato: ")).lower()
        for i in range(len(Contatos)):    
            if(i >= len(Contatos)):
                break		#evitando erro de out of range in "i".
            
            for z in (Contatos[i]):
                #print (z)  <-- teste de comportamento
                if z == Consulta:
                    print (f'Nome: {Contatos[i][0]}')
                    print (f'Tel: {Contatos[i][1]}')
                    print ()
                        
                    print ("1) Alterar dados do Contato.")
                    print ("2) Excluir contato.")
                    print ("3) Voltar ao inicio.")
                                
                    opcao2= int(input("Digite uma opção para continuar: "))# Selecionar uma opçao acima desta instrução

                    while opcao2!=1 and opcao2!=2 and opcao2!=3:  	# Opção inexistente das que estavam disponíveis (menu de alteração)
                        print("Opção inexistente!")          
                        opcao2= int(input("Digite a opção novamente: "))

                    if (opcao2 == 1):       # Opção Alterar dados do Contato
                        Contatos[i][0]= str(input("Nome: ")).lower()
                        Contatos[i][1]= str(input("Tel: "))
                        
                    elif (opcao2 == 2):     # Opção Remover contato
                        Contatos.pop(i)
                        break

                    elif (opcao2 == 3):		# Volta para o menu de seleção
                        print ("Voltando ao inicio...")  
                 
#--------------------------------------------------------------------------
                    
    elif opcao == 3:                            # Mostrar todos os Contatos.
        print ("__"* 18,"\n")
        print ("AGENDA")
        print ("----")
        for x in range(len(Contatos)):          # Varredura na lista contatos.
            print (f'Contato {x+1}:')
            print (f'Nome: {Contatos[x][0]}')
            print (f'Tel: {Contatos[x][1]}')
            print ("----")            

#--------------------------------------------------------------------------

    elif opcao == 4:    # Sair do Programa
        break           # Interrompe o Loop while True (rotina infinita do código).

#-------------------------------------------------------------------------
    
    else:
        print("Opção inexistente!")     # Opção diferente das que estavam disponíveis (menu de seleção)
                
                
            
    

    
    
