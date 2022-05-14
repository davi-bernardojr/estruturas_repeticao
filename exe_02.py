altura = []
maior = 0
menor = 999
ok = True

for i in range(5):
    ok = False
    while (ok == False):
        try:
            altura.append( float(input(f"Informe a altura da {i+1}° pessoa: ")) )
            ok = True
        except :
            print("Por favor informe apenas numero no padrão 0.00")
            ok = False

for i in range(len(altura)):
    if (maior < altura[i]):
        maior = altura[i]
    
    if (menor > altura[i]):
        menor = altura[i]
        
print(f"""A maior altura é {maior}
e a menor é {menor}""")