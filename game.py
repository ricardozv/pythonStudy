print("***********************************")
print("********Wellcome the game!!********")
print("***********************************")

numero_secreto = 42
chute = input("Digite seu número: ")
print ("Você digitou", chute)
chute = int(chute)

if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

print("End Game ")
