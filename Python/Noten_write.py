noten={
    "Nora": 87,
    "Gino": 100,
    "Loretto": 67,
    "Talina":45
}

with open("datei_studentensuper.txt","w") as file:
    for name,note in noten.items():
        file.write(name+"-"+str(note)+"\n")
        
    


#file=open("datei_studenten.txt","w")
#for name,note in noten.items():
#    file.write(name+"-"+str(note)+"\n")
        
    
#file.close()
