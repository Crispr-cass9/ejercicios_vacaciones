def revertir(string):
    print(string)
    if len(string) == 1:
        return string
    return revertir(string[1:]) + string[0]

print(revertir('mecanografía')) 