def main():
    n1=int(input("Escriba un número: "))
    n2=int(input(f"Escriba un número mayor que {n1}: "))

    while n2<=n1:
        n2=int(input(f"{n2} no es mayor que {n1}. Inténtelo de nuevo: "))
    
    print(f"Los números que ha escrito son {n1} y {n2}")


if __name__=="__main__":
    main()







          
