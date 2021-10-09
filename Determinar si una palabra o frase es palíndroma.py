frase=input("ingresa una palabra:")
frase=frase.lower()
frase=frase.replace(' ',' ')
logitud=len(frase)

pila1 = list(frase)
pila2=[]
pila3=[]

palindro= True
for i in range(len(pila1)):
    aux=pila1.pop()
    pila2.append(aux)
    pila3.append(aux)
for i in range(len(pila2)):
    aux=pila2.pop()
    pila1.append(aux)

for i in range(len(pila3)):
    aux=pila1.pop()
    aux2=pila3.pop()
    if (aux!=aux2):
        palindro=False
if(palindro==True):
    print("la palabra introducida SI es un palindromo")
else:
    print("la palabra introducida NO es un palindromo")