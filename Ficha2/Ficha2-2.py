num1 = int(input("Medida do lado1: "))
num2 = int(input("Medida do lado2: "))
num3 = int(input("Medida do lado3: "))

if(num1 == num2 and num3 == num1): print("Este triângulo é equilátero")

elif(num1 == num2 and num3 != num1 or num1 == num3 and num3 != num2): print("Este triângulo é isosceles")

else: print("Este triângulo é escaleno")