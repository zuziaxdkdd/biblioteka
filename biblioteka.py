import poboczne
import uuid

biblioteka = []

def dodawanieksiazki(lst:biblioteka) -> None:
    ksiazka = {
        "id" : uuid.uuid4(),
        "tytul" : "cos tam",
        "cena" : "40",
        "liczba stron" : 200
    }
    biblioteka.append(ksiazka)

#--------------------------------------------------

while True:
    poboczne.legenda()
    inp = input()
    if inp == "0":
        poboczne.inf(biblioteka)
    elif inp == "1":
        poboczne.edytujdane(biblioteka)
    elif inp == "2":
        poboczne.dodaj_ksiazke(biblioteka)
    elif inp == "3":
        poboczne.usunksiazke(biblioteka)
    elif inp == "4":
        print("---")
        break
    else:
        print("nie ma takiej komendy")
