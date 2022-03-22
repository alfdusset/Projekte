def verschüsseln(text):
    print("Der zu verschlüsselnde Text lautet: " + text)
    Endtext = ""
    for letra in text:
        Endtext += letra + "x"
    print(Endtext)
    return Endtext


def entschüsseln(text):
    print("Der zu entschlüsselnde Text lautet: " + text)
    Endtext = ""
    contador = 0
    for letra in text:
        if contador%2 == 0:
            Endtext += letra
        contador += 1
    print(Endtext)
    return Endtext


def encriptararchivo():
    file = open("text.txt", "r")
    texto = file.read()
    file.close()
    
    textoencriptado = verschüsseln(texto)

    file = open("text.txt","w")
    file.write(textoencriptado)
    file.close()

def desencriptararchivo():
    file = open("text.txt", "r")
    texto = file.read()
    file.close()
    
    textodesencriptado = entschüsseln(texto)

    file = open("text.txt","w")
    file.write(textodesencriptado)
    file.close()


desencriptararchivo()
