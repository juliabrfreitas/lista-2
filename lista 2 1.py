x=input("Digite o n�mero aqui")
string=str((2**x))
cont=0
for i in range(len(string)):
    numero=float(string[i])
    cont+=numero
print cont
