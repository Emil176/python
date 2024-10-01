def frågesport():
    antal_rätt = 0

    # Fråga 1
    print("Fråga 1: Vad heter Sveriges huvudstad?")
    print("1) Göteborg")
    print("2) Stockholm")
    print("3) Malmö")
    svar1 = input("Skriv 1, 2 eller 3: ")

    if svar1 == "2":
        print("Rätt!")
        antal_rätt += 1
    else:
        print("Fel.")

    # Fråga 2
    print("\nFråga 2: När vann AIK senast SM Guld i fotboll?")
    print("1) 2016")
    print("2) 2017")
    print("3) 2018")
    svar2 = input("Skriv 1, 2 eller 3: ")

    if svar2 == "3":
        print("Rätt!")
        antal_rätt += 1
    else:
        print("Fel.")

    # Fråga 3
    print("\nFråga 3: Vilket är världens längsta flod?")
    print("1) Nilen")
    print("2) Amazonas")
    print("3) Mississippi")
    svar3 = input("Skriv 1, 2 eller 3: ")

    if svar3 == "1":
        print("Rätt!")
        antal_rätt += 1
    else:
        print("Fel.")

    # Visa resultatet
    print(f"\nDu fick {antal_rätt} av 3 rätt.")

# Starta frågesporten
frågesport()
