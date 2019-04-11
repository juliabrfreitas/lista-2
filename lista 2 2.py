x=int(input("Digite o número máximo"))

lista=[1,1]
acumulador=2
if x>1:
    tn=0
    while tn<=x:
        tn=lista[-1]+lista[-2] #tn=termo novo
        if tn<=x:
            lista.append(tn)
    for i in range(len(lista)):
        if lista[i]%2==1:
            acumulador+=lista[i]
    print (acumulador)
else:
    print("2")
