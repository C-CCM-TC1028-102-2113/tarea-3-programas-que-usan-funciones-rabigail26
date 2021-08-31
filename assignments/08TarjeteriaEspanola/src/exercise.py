
def maximo(pliegos,plumones):
    tarjetaxpliego = pliegos * 12
    tarjetasxplumon = plumones * 35
    if tarjetaxpliego > tarjetasxplumon:
        total = tarjetasxplumon
    if tarjetaxpliego < tarjetasxplumon:
        total = tarjetaxpliego
    return total
def main():
    #escribe tu código abajo de esta línea
    pass
#Tarjetería Española


pliegos = int (input ("Dame la cantidad de pliegos de papel albanene: "))
plumones = int (input ("Dame la cantidad de plumones: "))
tarjetas = maximo(pliegos,plumones)
print ("El número máximo de tarjetas que se pueden hacer es: ", int(tarjetas))

if __name__=='__main__':
    main()
