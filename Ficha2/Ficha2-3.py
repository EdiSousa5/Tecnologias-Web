gen = str(input("Género(M/F): "))
alt = int(input("Alture(Cm): "))

if(gen == "M" or gen == "m"): k = 4

elif(gen == "S" or gen == "s"): k = 2

else:
    print("Inseriu o género mal!")
    exit()

ideal = (alt-100) - (alt-150)/k

print("O Peso ideal é", round(ideal,3), "Kg")