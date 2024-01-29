import uuid


def inf(lst:list)->None:
    for dic in lst:
        for v,k in dic.items():
            print(f"{v} : {k}")
        print("----"*20)

#------------------   LEGENDA   --------------------------------

def legenda() -> None:
    print("0 - informacje")
    print("1 - edytuj dane")
    print("2 - dodaj ksiazke ")
    print("3 - usun ksiazke")
    print("4 - wyjdz z programu")
    print("----"*20)

#-------------------  INF KSIAZKA BIBLIOTEKA   -------------------------------

def inf_ksiazki(dc):
    for k,v in dc.items():
        print(f"{k}  :  {v}")
        print("----"*20)


def inf_biblioteki(lst:list) -> None:
    print(f"liczba ksiazek = {len(lst)}")
    for ksiazka in lst:
        print("----"*20)
        inf_ksiazki(ksiazka)
        print("----"*20)


#--------------------  ID KSIAZKI  ------------------------------
    
def istnienieksiazki(lst: list, id_user_inp: str) -> bool:
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_user_inp:
            return True
    return False

def index_instniejacej_ksiazki(lst: list, id_user_inp: str) -> int:
    for i in range(len(lst)):
        if str(lst[i]["id"]) == id_user_inp:
            return i
    return -1 

#-------------------  DANE KSIAZKI  -------------------------------

def tytul()-> str:
    print("podaj tytul ksiazki")
    inp = input("tytul -  ")
    return inp

def cena()-> float:
    print("podaj cene ksiazki")
    inp = float(input("cena -  "))  
    return inp

def liczbastron()-> int:
    print("podaj liczbe stron ksiazki")
    inp = int(input("liczba stron: "))
    return inp

#-----------------  DODAWANIE KSIAZKI  ---------------------------------

def dodaj_ksiazke(lst: list)-> None:
    ksiazka = {
        "id" : uuid.uuid4(),
        "tytul" : tytul(),
        "cena" : cena(),
        "liczba stron" : liczbastron()
    }
    lst.append(ksiazka)

#-----------------  EDYTOWANIE KSIAZKI  ---------------------------------

def edytujdane(lst:list) -> None:
    inf_biblioteki(lst)
    inp = input("wprowadz id ksiazki -  ")
    if istnienieksiazki(lst, inp):
        index_ksiazki = index_instniejacej_ksiazki(lst, inp)
        lst[index_ksiazki]["tytul"] = tytul()
        lst[index_ksiazki]["cena"] = cena()
        lst[index_ksiazki]["liczba_stron"] =liczbastron()
    else:
        print("nie ma ksiazki z takim id")

#----------------------  USUWANIE KSIAZKI  ----------------------------

def usunksiazke(lst: list) -> None:
    inf_biblioteki(lst)
    inp = input("podaj id ksiazki: ")
    if istnienieksiazki(lst, inp):
        index = index_instniejacej_ksiazki(lst, inp)
        if index != -1:
            lst.pop(index)
            print("ksiazka zostala usunieta")
        else:
            print("ksiazka nie istnieje")
    else:
        print("nie ma ksiazki z takim id")