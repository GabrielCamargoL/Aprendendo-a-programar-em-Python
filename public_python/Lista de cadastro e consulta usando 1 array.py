#   1) Faça um programa de Agenda usando Lista.
#      O programa deve ter um menu que permita:
#           
#           1- Cadastrar
#           2- Consultar
#           3- Mostrar todos contatos
#           4- Sair
#-------------------------------------------------------------------------
#   2) Inclua o cadastro do telefone no mesmo array.
#-------------------------------------------------------------------------
#   3) Na opção Consulta ofereça as opçoes alterar e excluir. Use a função
#      Remove para excluir |("lista.remove ('item da lista')|
#                          |  lista.pop(index)              |
#                          |  del lista[index]              |
#-------------------------------------------------------------------------

Contatos= []
contador= int(0)
y= int(0)
x= str('')
while True:
    
    print (37* "__")     # Quebra de linha para melhor visualização :)
    print ()             #
    
    print ("1) Cadastrar.")
    print ("2) Consultar.")
    print ("3) Mostrar todos os contatos")
    print ("4) Sair")

    print ()

    opcao= int(input("Digite uma opcao para avançar: "))

#--------------------------------------------------------------------------

    if opcao == 1:
        nome =str(input("Digite o nome do contato: "))
        tel = int(input("Digite o telefone do contato"))
        
        linha= [nome,tel]
        Contatos.append(linha)
        
#--------------------------------------------------------------------------

    elif opcao == 2:
        Consulta= str(input("Digite o nome do contato: "))
        for i in range(len(Contatos)):    
            if(i >= len(Contatos)):
                break
            
            for x in (Contatos[i]):
                #print (x)
                if x == Consulta:
                    print (Contatos[i])
                    print ()
                        
                    print ("1) Alterar dados do Contato.")
                    print ("2) Excluir contato.")
                    print ("3) Voltar ao inicio.")
                                
                    opcao2= int(input("Digite uma opção para continuar: "))# Selecionar uma opçao acima desta instrução

                    while opcao2!=1 and opcao2!=2 and opcao2!=3:  # Opção inexistente das que estavam disponíveis (menu de alteração)
                        print("Opção inexistente!")          
                        opcao2= int(input("Digite a opção novamente: "))

                    if (opcao2 == 1):       # Opção Alterar dados do Contato
                        Contatos[i][0]= str(input("Digite o nome do contato: "))
                        Contatos[i][1]= int(input("Digite o telefone do contato"))
                        
                    elif (opcao2 == 2):     # Opção Remover contato
                        Contatos.pop(i)
                        break

                    elif (opcao2 == 3):
                        print ("Voltando ao inicio...")     # Volta para a sessão de seleção de tarefa
                 
#--------------------------------------------------------------------------
                    
    elif opcao == 3:                # Mostrar todos os Contatos.
        print ("__"* 37)
        print ("Contatos / Telefones")
        for x in Contatos:          # Varredura na lista contatos.
            y= Contatos.index(x)
            print (*Contatos[y])

#--------------------------------------------------------------------------

    elif opcao == 4:    # Sair do Programa
        break           # Interrompe o Loop while True (rotina infinita do código).

#-------------------------------------------------------------------------
    
    else:
        print("Opção inexistente!")     # Opção diferente das que estavam disponíveis (menu de seleção)
                
                
            
    

    
    
