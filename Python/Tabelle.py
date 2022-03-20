blatt=open("Tabelle.txt","w")

for i in range(1,11):
    print()
    print(file=blatt)
    for x in range(1,11):
        print(i*x,end="\t")
        print(i*x,end="\t",file=blatt)

blatt.close()
