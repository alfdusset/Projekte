
def calcula_media(*args):
    total=0

    for i in args:
        total+=i

    resultado=total/len(args)
    return resultado
    
    


a,b,c,=3,4,5
media=calcula_media(a,b,c)
print(f"La media de {a},{b} y {c} es: {media}")
print("Programa terminado")
    


