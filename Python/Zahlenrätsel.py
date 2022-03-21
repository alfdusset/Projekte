from random import randint

a=randint(1,101)
b=0

while b==0:
    Frage=int(input(f"Geben Sie eine Zahl zwischen 1 und 100 ein: "))

    if Frage>a:
        print(f"Die Zahl ist GRÖSSER als die unbekannte Zahl.")
        print()
        
    elif Frage<a:
        print(f"Die Nummer ist KLEINER als die unbekannte Nummer.")
        print()
        
    else:
        print(f"SIE HABEN DIE NUMMER RICHTIG!!!")
        print()
        b+=1

print(f"Ausführung beendet.")
print()
