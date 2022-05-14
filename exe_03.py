decisao = 0
num_positivos = []
num_negativos = []
media = 0
ok = False
ok_if = False
num = 0

while (ok == False):
    ok_if = False
    try :
        decisao = int(input("""escolha uma opção:
            1 - Informar um numero.
            2 - Média dos valores.
            3 - Total de valores positivos.
            4 - Total de valores negativos.
            5 - Percentual de valores positivos.
            6 - Percentual de valores negativos.
            0 - Para sair."""))
        if (decisao > 6) : 
            raise ValueError
    except(ValueError) :
        print("Opção inválida.")
    except : 
        print("informe um valor da lista.")
        
    if (decisao == 0) :
        break
    elif (decisao == 1) :
        while (ok_if == False) :
            try :
                num = 0
                num = float(input("Informe um numero positivo ou negativo."))
                if (num >= 0):
                    num_positivos.append(num)
                else :
                    num_negativos.append(num)
                ok_if = True
            except :
                print("Informe apenas numeros positivo ou negativo no padrão 0.00.")
    elif (decisao == 2) :
        for i in range(len(num_negativos)):
            media += num_negativos[i]
        for i in range(len(num_negativos)):
            media += num_positivos[i]
        if(media == 0 ):
            print("""A soma dos numeros positivos e negativos 
é igual a 0, portanto não pode ser calculada a média.""")
        else :
            print(f"A média é {(media / (len(num_positivos) + len(num_negativos)))}")
    elif (decisao == 3) :
        print(f"O total de valores positivos é {len(num_positivos)}")
    elif (decisao == 4) :
        print(f"O total de valores negativos é {len(num_negativos)}")
    elif (decisao == 5) :
        if (len(num_positivos) == 0) :
            print("Não foi inserido nenhum valor positivo.")
        else :
            num = len(num_positivos) / (len(num_positivos) + len(num_negativos)) * 100 
            print(f"O percentual de valores positivos {num:.2f}")
    elif (decisao == 6) :
        if (len(num_negativos) == 0) :
            print("Não foi inserido nenhum valor positivo.")
        else :
            num = len(num_negativos) / (len(num_positivos) + len(num_negativos)) * 100
            print(f"O percentual de valores positivos {num:.2f}")
        
        
        
        
        