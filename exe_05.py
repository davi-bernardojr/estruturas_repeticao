intervalo = []
pares = 0
impares = 0
media_pares = 0
media_geral = 0
decisao = False

while (decisao == False) :
    try :
        num = int(input("Informe um numero inteiro positivo.\nInforme 0 para terminar. "))
        if ( num == 0):
            break
        elif (num < 0):
            print("O numero informado deve ser positivo e sem ponto.")
        else :
            intervalo.append(num)
    except :
        print("Informe apenas um numero inteiro sem ponto ou virgula.")

for i in range(len(intervalo)):
    if (intervalo[i] % 2 == 0) :
        media_pares += intervalo[i]
        pares += 1
    else :
        impares += 1
    media_geral += intervalo[i]
    
print(f"""Quantidade de numeros pares: {pares}
Quantidade de numeros impares: {impares}
A media de valores pares: {media_pares/pares:.2f}
A media geral de valores: {media_geral/len(intervalo):.2f}""")