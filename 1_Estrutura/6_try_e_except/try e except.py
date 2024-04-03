num1  = input("digite um numero")
num2  = input("digite um numero")

try:  # tente executar, se ocorre um erro pula para o except
    num1 = float(num1)
    num2 = float(num2)

    print(num1+num2)
except:
    print("error")