
zeronove= ["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]

dezvinte= ["dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"]

deznoventa = ["dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]

cemnovecentos=["cem","duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"]


def Extenso(n):
    nstr=str(n)
    nstrr=nstr.zfill(5)
    n5=int(nstrr[0])
    n4=int(nstrr[1])
    n3=int(nstrr[2])
    n2=int(nstrr[3])
    n1=int(nstrr[4])
    if n<=99:
        return Funcao1(n1,n2)
    if n>99 and n<=999:
        return Funcao2(n1,n2,n3)
    if n>999 and n<=99999:
        return Funcao3(n1,n2,n3,n4,n5)


def Funcao1(n1,n2):
    if n2==0:
        extenso=zeronove[n1]
        return extenso
    if n2==1:
        extenso=dezvinte[n1]
        return extenso
    if n2>=2 and n2<=9:
        if n1==0:
            extenso=deznoventa[n2-1]
            return extenso
        else:
            extenso=deznoventa[n2-1]+ " e " +zeronove[n1]
            return extenso

def Funcao2(n1,n2,n3):
    if n2==0 and n1==0:
        extenso=cemnovecentos[n3-1]
        return extenso
    else:
        if n3==1:
            extenso="cento e "+ Funcao1(n1,n2)
            return extenso
        if n3>=2 and n3<=9:
            extenso=cemnovecentos[n3-1]+" e "+Funcao1(n1,n2)
            return extenso

def Funcao3(n1,n2,n3,n4,n5):
    if n5==0 and n4==1:
        extenso="mil e "+Funcao2(n1,n2,n3)
        return extenso        
    else:
        extenso=Funcao1(n4,n5)+" mil e "+Funcao2(n1,n2,n3)
        return extenso

    
n=int(input("Digite o número aqui"))
if n<=99999:
    print (Extenso(n))
else:
    print ("digite um número menor que 99999")
