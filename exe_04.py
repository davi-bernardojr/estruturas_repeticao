intervalo = [[], [], [], []]
decisao = False

while (decisao == False) :
    try :
        num = int(input("Informe um numero inteiro.\nInforme um numero negativo para terminar "))
        if ( num < 0):
            break
        else:
            if (num > 0 and num <= 25):
                intervalo[0].append(num)
            elif (num >= 26 and num <= 50):
                intervalo[1].append(num)
            elif (num >= 51 and num <= 75):
                intervalo[2].append(num)
            elif (num >= 76 and num <= 100):
                intervalo[3].append(num)
            else :
                print("Numero fora da faixa aceitavel.\nInforme um numero entre 0 e 100 ou um numero negativo para sair.")
    except :
        print("Informe apenas um numero inteiro sem ponto ou virgula.")

print(f"""Numeros na faixa [0-25] - {len(intervalo[0])}
Numeros na faixa [26-50] - {len(intervalo[1])}
Numeros na faixa [51-75] - {len(intervalo[2])}
Numeros na faixa [76-100] - {len(intervalo[3])}""")