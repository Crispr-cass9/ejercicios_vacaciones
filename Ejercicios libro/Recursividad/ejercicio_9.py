def contar_digitos(n):
    if n/10<1:
        return 1
    return contar_digitos(n/10) +1

print(contar_digitos(1234886234))
#--> 10