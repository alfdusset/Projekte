teiler=[]
zahl=int(input("Bitte, geben Sie ein Zahl ein:"))
a=zahl

while a!=0:
    if zahl%a==0:
        teiler.append(a)

    a-=1

print("Die Teilen von",zahl,"sind",teiler)
print("Die Zahl",zahl,"hat",len(teiler),"Teiler")
    

    


        
