#   1) Fazer uma calculadora básica, usando Python.

while True:
    Resultado = float(0)

    print ("__"* 37)
    print ()
    
    N1= float(input("Digite o primeiro numero: "))
    N2= float(input("Digite o segundo numero: "))
    
    print ()
    print("[+] -> Adição")
    print("[-] -> Subtração")
    print("[*] -> Multiplicação")
    print("[/] -> Divisão")
    print ()

    opcao= str(input("Digite o tipo de operação que deseja executar: "))
    
#----------------------------------------------------------------------------------------   

    while (opcao != "+") and  (opcao != "-") and (opcao != "*") and (opcao != "/"):
        print ("Opção inexistente!")
        opcao= str(input('\033[0;31mDigite a operação novamente ( +  -  *  / ):\033[m'))

    if opcao == "+":           
        Resultado= N1+N2

    elif opcao == "-":           
        Resultado= N1-N2

    elif opcao == "*":           
        Resultado= N1*N2

    elif opcao == "/":
        Resultado= N1/N2

    print ()    
    print (f'\033[1;32m{N1} {opcao} {N2} = {Resultado:.2f}\033[m')

#----------------------------------------------------------------------------------------
    
                 

    
