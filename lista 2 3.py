def NumeroPrimo(n):
    cont=0
    for i in range(2,n):
        if n%i!= 0:
            cont=cont+1
        else:
            cont=cont
    if cont==(n-2)or n==1:
        return True
    else:
        return False


def Rotina(x=3852914583882):
    maior=0
    for i in range (1,x+1):
        if x%i==0:
            if NumeroPrimo(i):
                maior=i
    print (maior)

Rotina()
