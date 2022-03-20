def main():
    n1=int(input(f"Escriba un número par: "))

    while n1%2!=0:
        n1=int(input(f"{n1} no es número par. Inténtelo de nuevo: "))

    n2=str(input(f"Quiere escribir otro número par? (S/N): "))

    while n2!="S" and n2!="s" and n2!="N" and n2!="n":
        n2=str(input(f"Quiere escribir otro número par? (S/N): "))

    print(f"Ha escrito {n1}")


if __name__=="__main__":
    main()
    


    
