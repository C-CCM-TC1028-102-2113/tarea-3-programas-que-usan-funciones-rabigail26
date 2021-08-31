def añobisiesto():
    if 0 ==  año % 4:
        print ("Verdadero")
    else:
        if 0== (año % 100) or (año % 400):
            print ("Falso")

def main():
    #escribe tu código abajo de esta línea
    pass
#Año bisiesto



año = int(input("Dame el año"))
añobisiesto()

if __name__=='__main__':
    main()
