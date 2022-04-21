Segunda = input("Insira o numero de votos do dia Segunda:")
Terça = input("Insira o numero de votos do dia Terça:")
Quarta = input("Insira o numero de votos do dia Quarta:")
Quinta = input("Insira o numero de votos do dia Quinta")
Sexta = input("Insira o numero de votos do dia Sexta:")
if int(Segunda) > int(Terça):
    if int(Segunda) > int(Quarta):
        if int(Segunda) > int(Quinta):
            if int(Segunda) > int(Sexta):
                print("O dia mais votado foi Segunda-Feira")

elif int(Terça) > int(Segunda):
    if int(Terça) > int(Quarta):
        if int(Terça) > int(Quinta):
            if int(Terça) > int(Sexta):
                print("O dia mais votado foi Terça-Feira")

if int(Quarta) > int(Segunda):
    if int(Quarta) > int(Terça):
        if int(Quarta) > int(Quinta):
            if int(Quarta) > int(Sexta):
                print("O dia mais votado foi Quarta-Feira")

elif int(Quinta) > int(Segunda):
    if int(Quinta) > int(Terça):
        if int(Quinta) > int(Quarta):
            if int(Quinta) > int(Sexta):
                print("O dia mais votado foi Quinta-Feira")

if int(Sexta) > int(Segunda):
    if int(Sexta) > int(Terça):
        if int(Sexta) > int(Quarta):
            if int(Sexta) > int(Quinta):
                print("O dia mais votado foi Sexta-Feira")





