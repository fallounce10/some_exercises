import sys

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def division(x,y):
    return x / y

def multiplication(x,y):
    x * y

print("******Python Calculator*******")
print("Selecione o número da opção desejada:")
print()
print("1-Soma")
print("2-Subtração")
print("3-Multiplicação")
print("4-Divisão")
print()
user_input = int(input("Digite a sua opção (1/2/3/4): "))

if user_input <= 0 or user_input > 4:
    print("Input inválido")
    sys.exit()

num_one = int(input("Number 1: "))
num_two = int(input("Number 2: "))

if user_input == 1:
    print(f"{num_one}+{num_two}={num_one+num_two}")
elif user_input == 2:
    print(f"{num_one}-{num_two}={num_one+num_two}")
elif user_input == 3:
    print(f"{num_one}*{num_two}={num_one+num_two}")
else:
    print(f"{num_one}/{num_two}={num_one+num_two}")
