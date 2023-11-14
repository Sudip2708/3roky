from insured import Insured
import time

def add_new_insured():
    """
    Metoda si vyžádá povinné údaje a zavolá třídu pro vložení údajů do databáze
    :return: None
    """
    print("Zadání údajů nového pojištěnce:")
    name = input("Křestní jméno: ").strip()
    surname = input("Příjmení: ").strip()
    phone = int(input("Telefon: ").strip())
    age = int(input("Věk: ").strip())
    Insured(name, surname, phone, age)
    print("--------------------------------------------------")
    print("Do databáze byl přidán záznam:")
    print(f"Jméno: {name}, Příjmení: {surname}, Telefon: {phone}, Věk: {age}")
    print("--------------------------------------------------")
    _input_1234()


def print_all_insured():
    """
    Metoda vypíše všechny pojištěnce
    :return: seznam všech pojištěnců
    """
    if Insured._list_of_ensured != []:
        print("Výpis databáze:")
        for one_tuple in Insured._list_of_ensured:
            for one_item in one_tuple:
                print(one_item, end=", ")
            print()
        print("--------------------------------------------------")
    else:
        print("Databáze je prázdná.")
    _input_1234()

def print_one_insured():
    """
    Metoda si vyžádá jméno a příjmení
    a najde-li je v databázy, vrátí další hodnoty
    :return:
    """
    print("Vyplňte následující 2 údaje týkající se hledaného pojištěnce:")
    name = input("Křestní jméno: ").strip().lower()
    surname = input("Příjmení: ").strip().lower()
    finds = []

    for one_tuple in Insured._list_of_ensured:
        if one_tuple[0].strip().lower() == name and one_tuple[1].strip().lower() == surname:
            finds.append(one_tuple)
    if len(finds) != 0:
        print("--------------------------------------------------")
        print("Nalezené záznamy v databáze:")
        for one_tuple in finds:
            for one_item in one_tuple:
                print(one_item, end=", ")
            print()
        print("--------------------------------------------------")
    else:
        print("--------------------------------------------------")
        print("Pro zadané údaje nebyl nalezen žádný záznam")
        print("--------------------------------------------------")
    _input_1234()



def exit_application():
    """
    Metoda vypíše oznam o ukončení programu a ukončí program.
    :return: None
    """
    print("Probíhá ukončení programu.")
    print("Děkujeme za použití.")
    print("Přejeme hezký zbytek dne!")
    print("--------------------------------------------------")
    time.sleep(3)
    exit()

def _input_1234() -> int:
    """Metoda si vyžádá zadání čísla od 1 do 4,
    ověří platnost vstupní hodnoty,
    vypíše oznam o zvolené možnosti,
    a zavolá příslušnou metodu k provedení zadaného příkazu."""

    while ...:
        print("Zadejte číslo úkonu (1-4),")
        entry_number = input("nebo zmáčkněte [enter] pro nápovědu: ").strip()
        if entry_number == '':
            print("--------------------------------------------------")
            print("Výběr možností:")
            print("1 - Přidat nového pojištěného")
            print("2 - Vypsat všechny pojištěné")
            print("3 - Vyhledat pojištěného")
            print("4 - Konec")
            print("--------------------------------------------------")
        else:
            try:
                if int(entry_number) in (1, 2, 3, 4):
                    entry_number = int(entry_number)
                    break
                else:
                    print("--------------------------------------------------")
                    print("Nezadali jste správné číslo, zkuste to znovu!")
                    print("--------------------------------------------------")
                    _input_1234()
            except ValueError:
                print("--------------------------------------------------")
                print("Nezadali jste celé číslo, zkuste to znovu!")
                print("--------------------------------------------------")

    if entry_number in (1, 2, 3, 4):
        match entry_number:
            case 1: selected_option = ">> Přidat nového pojištěného <<"
            case 2: selected_option = ">> Vypsat všechny pojištěné <<"
            case 3: selected_option = ">> Vyhledat pojištěného <<"
            case 4: selected_option = ">> Konec programu <<"

    print("--------------------------------------------------")
    print(f"Vybrali jste možnost {entry_number}: {selected_option}")
    print("--------------------------------------------------")

    match entry_number:
        case 1: add_new_insured()
        case 2: print_all_insured()
        case 3: print_one_insured()
        case 4: exit_application()



print("==================================================")
print(">>> Evidence pojištěných <<<")
print("--------------------------------------------------")
_input_1234()






