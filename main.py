# Deklarer og initialiserer 2 str variabler
tal1 = ""
tal2 = ""

# Kører programmet i et uendeligt loop
while True:
    
    print("\n" + "Indtast 2 tal som du vil plusse: (skriv exit for at afslutte)")

    # Tager imod det første tal som input
    tal1 = input("Tal 1: ")

    # Hvis tal1 er exit afslutter programmet 
    if tal1 == "exit":
        break
    
    # Konverterer tal1 til int og gemmer det i tal1ToInt
    tal1ToInt = int(tal1)

    # Tager imod det andet tal som input
    tal2 = int(input("Tal 2: "))

    # Hvis tal2 er exit afslutter programmet 
    if tal2 == "exit":
        break
    
    # Konverterer tal2 til int og gemmer det i tal2ToInt
    tal2ToInt = int(tal2)

    # Plusser de 2 tal sammen og gemmer det i result
    result = tal1ToInt + tal2ToInt

    # Konverterer result til str og gemmer det i resultToStr
    resultToStr = str(result)

    # Udskriver resultatet
    print("Resultat: " + resultToStr)