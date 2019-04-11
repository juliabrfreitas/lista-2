def Menu():
    print (" 1-Soma Vetores \n 2-Diferenca de Vetores \n 3-Sair")
    



def Opcao(v1,v2):
    while True:
        Menu()
        n=input("Digite a opcao aqui")
        if n=='3':
            break
        if n=='2' or n=='1':
            
            if n=='2':
                print (v1-v2)
            if n=='1':
                print (v1+v2)

Opcao(v1,v2)
