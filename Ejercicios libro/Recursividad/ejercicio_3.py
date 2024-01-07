def multiplicacion(a,b):
    if b==1:
        return a
    return a + multiplicacion(a, b-1)

print(multiplicacion(5, 4))
#--> 20