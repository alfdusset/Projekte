neuen_noten={
    "Emily":54,
    "Daniel":98,
    "Julienne":78,
}

with open("datei_studenten.txt","a") as file:
    for name,note in neuen_noten.items():
        file.write(name+"-"+str(note)+"\n")

