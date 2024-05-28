def multiplicar(a, b):
    if a < b:
        menor, maior = a, b
    else:
        menor, maior = b, a

    resultado = 0
    somas = []


    for _ in range(abs(menor)):
        resultado += maior
        somas.append(maior)


    if menor < 0:
        resultado = -resultado
        somas = [-maior for maior in somas]

    return resultado, somas

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado, somas = multiplicar(num1, num2)

print(f"{num1} * {num2} = {resultado}")
print("Operação: ", " + ".join(map(str, somas)))
