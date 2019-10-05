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
y= int (0)
x= str ('')
while True:
    
    print ()             #
    print (37* "__")     # Quebra de linha para melhor visualização :)
    print ()             #
    
    print ("1) Cadastrar.")
    print ("2) Consultar.")
    print ("3) Mostrar todos os contatos")
    print ("4) Sair")

    print ()             #
    print (37* "__")     # Quebra de linha para melhor visualização :)
    print ()             #

    opcao= int(input("Digite uma opcao para avançar: "))

#--------------------------------------------------------------------------

    if opcao == 1:
        linha= [(str(input("Digite o nome do contato: "))),(int(input("Digite o telefone do contato")))]
        Contatos.append(linha)
        
#--------------------------------------------------------------------------

    elif opcao == 2:
        Consulta= str(input("Digite o nome do contato: "))
        for x in Contatos[contador][0]:
            if x == Consulta:
                y= int(Contatos.index(x))
                print (*Contatos[y])
            else:
                contador+= 1
        
            print ()
            print ("1) Alterar dados do Contato.")
            print ("2) Excluir contato.")
            print ("3) Voltar ao inicio.")
                
            opcao2= int(input("Digite uma opção para continuar: "))# Selecionar uma opçao acima desta instrução

            if (opcao2 == 1):   # Opção Alterar dados do Contato
                Contatos.pop(y)
                linha= [(str(input("Digite o nome do contato: "))),(int(input("Digite o telefone do contato")))]
                Contatos.append(linha)

            elif (opcao2 == 2): # Opção Remover contato
                Contatos.pop(y)

            elif (opcao2 == 3):
                print ("Voltando ao inicio...")     # Volta para a sessão de seleção de tarefa
                    
            else:
                print("Opção inexistente!")         # Opção inexistente das que estavam disponíveis (menu de alteração)
                print ("Voltando ao inicio...")
                
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
        print("Opção inexistente!") # Opção diferente das que estavam disponíveis (menu de seleção)
                
                
            
    

    
    
