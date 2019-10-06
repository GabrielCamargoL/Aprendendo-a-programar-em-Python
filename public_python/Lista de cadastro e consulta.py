#   1) Faça um programa de Agenda usando Lista.
#      O programa deve ter um menu que permita:
#           
#           1- Cadastrar
#           2- Consultar
#           3- Mostrar todos contatos
#           4- Sair
#-------------------------------------------------------------------------
#   2) Inclua o cadastro de telefone num array aparte.
#-------------------------------------------------------------------------
#   3) Na opção Consulta ofereça as opçoes alterar e excluir. Use a função
#      Remove para excluir |("lista.remove ('item da lista')|
#                          |  lista.pop(index)              |
#                          |  del lista[index]              |
#-------------------------------------------------------------------------

Contatos= []
Telefones= []
Consulta= int(0)
x= int(0)
y= int(0)

#-------------------------------------------------------------------------

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
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    if opcao == 1:  #Cadastro
        Contatos.append(str(input("Digite um nome para o cadastro: "))) # Adiciona o nome cadastrado para a lista Contatos[nome]
        Telefones.append(int(input("Digite o telefone deste contato para o cadastro: ")))   # Adiciona o telefone cadastrado para a lista Telefones[telefone]
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif opcao == 2:                                        # Consulta seguido de alteração e exclusão de um item
        Consulta= str(input("Digite o nome do contato: "))
        for x in Contatos:                                  # Varredura de dados contados na lista
            if Consulta == x:                               # Condição de dado procurado e encontrado                        
                y= Contatos.index(x)                       # Ligação entre a lista de contato e de telefones          
                print (x,Telefones[y])                      # Apresentação do Contato e seu respectivo telefone
                
                print ("1) Alterar dados do Contato.")
                print ("2) Excluir contato.")
                print ("3) Voltar ao inicio.")
                opcao2= int(input("Digite uma opção para continuar: "))                 # Selecionar uma opçao acima desta instrução

                if (opcao2 == 1):               # Opção Alterar dados do Contato
                    Contatos.remove(Consulta)                                           # Remove o nome para alteração
                    del Telefones[y]                                                    # Remove o nome para alteração
                    Contatos.append(str(input("Digite o nome para alterar: ")))         # Adiciona um nome para alterar
                    Telefones.append(int(input("Digite o telefone para alterar: ")))    # Adiciona um telefone para alterar      
                
                elif (opcao2 == 2):             # Opção Remover contato
                    Contatos.remove(Consulta)   #
                    del Telefones[y]            # Apenas remove sem alteração

                elif (opcao2 == 3):
                    print ("Voltando ao inicio...")     # Volta para a sessão de seleção de tarefa
                    
                else:
                    print("Opção inexistente!")         # Opção inexistente das que estavam disponíveis (menu de alteração)
                    print ("Voltando ao inicio...")
                

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif opcao == 3:                # Mostrar todos os Contatos.
        print ("__"* 37)
        print ("Contatos / Telefones")
        for z in Contatos:          # Varredura na lista contatos.
            w= Contatos.index(z)    # Atribui o indice do Nome da lista à "y".
            print ()
            print (Contatos [w], Telefones[w])  # Usa o indice em INT de y para printar os elementos da lista.
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif opcao == 4:                # Sair do Programa

        break                       # Interrompe o Loop while True (rotina infinita do código).
#-------------------------------------------------------------------------
    else:
        print("Opção inexistente!")         # Opção diferente das que estavam disponíveis (menu de seleção)
        
