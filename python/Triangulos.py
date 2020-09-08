def triangulo(a, b, c): #Calcula o tipo de triangulo
    if(a==b and b==c):
        print("Triangulo equilatero")
    elif (a==b and a != c):
        print("Triangulo isósceles")
    else:
        print("Triangulo escaleno")

ladoA = input("Digite o lado A: ") #Recebe os lados do triangulo
ladoB = input("Digite o lado B: ")
ladoC = input("Digite o lado c: ")

ladoA = eval(ladoA) #Converte os lados para número
ladoB = eval(ladoB)
ladoC = eval(ladoC)

listTriangulo=[ladoA,ladoB,ladoC]   #Converte o triangulo em listas e
listTriangulo=sorted(listTriangulo) #ordena a lista 

#Com a lista ordenada, o maior número sempre será o indice 2
#assim sendo possível realizar a verificação se os dados passados
#são ou não um triangulo, concluindo o programa
if listTriangulo[2]>=listTriangulo[0]+listTriangulo[1]: 
    print("Não é um triangulo")

else:
    triangulo(listTriangulo[0], listTriangulo[1], listTriangulo[2])
