try:
    idade = int(input("Informe a Idade: "))
    tempo = int(input("Informe o Tempo Trabalhado: "))
except ValueError:
    print("Verifique os dados informados")
else:
    if idade >= 65:
        print("Você está APTO")
    elif tempo >= 30:
        print("Você está APTO")
    elif idade >= 60 and tempo >= 25:
        print("Você está APTO")
    else:
        print("Você está INAPTO")
    