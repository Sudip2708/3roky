import tkinter
from tkinter import ttk
import db

class NextWindow:

    def __init__(self, window_name, window_size):
        # vytvoření základního okna
        next_window = tkinter.Tk()
        next_window.title(window_name)
        next_window.geometry(window_size)
        # přidání stylu (k tabulce)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background="light gray")
        # vytvoření základního rámu
        self._frame = tkinter.Frame(next_window)
        self._frame.pack()
        # vytvoření pole pro hledání
        self.create_search_entry()
        # vytvoření pole pro výsledky hledání
        # smyčka hlavního okna
        next_window.mainloop()

    def get_search_data(self):
        # Získání dat:
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        zip = self.zip_entry.get()
        # vytvoření dotazu:
        row_condition = None
        list_of_column_name = ['name', 'surname', 'email', 'phone', 'address', 'city', 'zip']
        list_of_column_entry = [name, surname, email, phone, address, city, zip]
        for index, entry in enumerate(list_of_column_entry):
            if entry:
                if row_condition:
                    row_condition += " AND "
                else:
                    row_condition = ""
                row_condition += f"{list_of_column_name[index]} LIKE '{entry+'%'}'"
        print(row_condition)
        # odeslání dotazu do databáze a uložení výsledku do atributu _table_content
        self._table_content = db.get_table_data('database.db', 'the_insured', row_condition=row_condition)
        print(self._table_content)
        # aktualizace dat ve výstupní tabulce
        self.update_table()

    def create_search_entry(self):
        # Proměné pro výpis
        name = 'Anit'
        surname = 'Banit'
        email = 'anit@banit.cz'
        phone = 420598512363
        address = 'U hospody 9'
        city = 'Krumlov'
        zip = 58231



        # vytvoření rámu pro iunformační okno
        user_info_frame = tkinter.LabelFrame(self._frame, text="Detail pojištěnce")
        # umístnění rámu pro vyhledávací okno v rodičovském rámu
        user_info_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=5)
        # lokální proměnné pro spadávky a umístění
        padx = 14
        pady = 5
        sticky = "e"
        sticky2 = "w"
        width = 6
        width2 = 16

        # vytvoření popisku a zadávacího pole pro jméno
        name_label = tkinter.Label(user_info_frame, text="Jméno:", width=width)
        name_label.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
        self.name_entry = tkinter.Label(user_info_frame,text="Dalibor", width=width2)
        #self.name_entry = tkinter.Entry(user_info_frame)
        self.name_entry.grid(row=0, column=1, sticky=sticky2, padx=padx, pady=pady)

        # vytvoření popisku a zadávacího pole pro příjmení
        surname_label = tkinter.Label(user_info_frame, text="Příjmení:", width=width)
        surname_label.grid(row=0, column=2, sticky=sticky, padx=padx, pady=pady)
        self.surname_entry = tkinter.Label(user_info_frame, text="Sova", width=width2)
        #self.surname_entry = tkinter.Entry(user_info_frame)
        self.surname_entry.grid(row=0, column=3, sticky=sticky2, padx=padx, pady=pady)

        # vytvoření popisku a zadávacího pole pro ID
        name_label = tkinter.Label(user_info_frame, text="ID:", width=width)
        name_label.grid(row=0, column=4, sticky=sticky, padx=padx, pady=pady)
        self.name_entry = tkinter.Label(user_info_frame,text="27", width=width2)
        #self.name_entry = tkinter.Entry(user_info_frame)
        self.name_entry.grid(row=0, column=5, sticky=sticky2, padx=padx, pady=pady)

        # vytvoření popisku a zadávacího pole pro email
        email_label = tkinter.Label(user_info_frame, text="Email:", width=width)
        email_label.grid(row=1, column=0, sticky=sticky, padx=padx, pady=pady)
        self.email_entry = tkinter.Label(user_info_frame, text="daliborsova@seznam.cz", width=width2)
        #self.email_entry = tkinter.Entry(user_info_frame)
        self.email_entry.grid(row=1, column=1, sticky=sticky2, padx=padx, pady=pady)

        # vytvoření popisku a zadávacího pole pro telefon
        phone_label = tkinter.Label(user_info_frame, text="Telefon:", width=width)
        phone_label.grid(row=1, column=2, sticky=sticky, padx=padx, pady=pady)
        self.phone_entry = tkinter.Label(user_info_frame, text="+420 704 564 595", width=width2)
        #self.phone_entry = tkinter.Entry(user_info_frame)
        self.phone_entry.grid(row=1, column=3, sticky=sticky2, padx=padx, pady=pady)

        # vytvoření popisku a zadávacího pole pro adresu
        address_label = tkinter.Label(user_info_frame, text="Adresa:", width=width)
        address_label.grid(row=2, column=0, sticky=sticky, padx=padx, pady=pady)
        self.address_entry = tkinter.Label(user_info_frame, text="Štúrova 591/24", width=width2)
        #self.address_entry = tkinter.Entry(user_info_frame)
        self.address_entry.grid(row=2, column=1, sticky=sticky2, padx=padx, pady=pady)

        # vytvoření popisku a zadávacího pole pro město
        city_label = tkinter.Label(user_info_frame, text="Město:", width=width)
        city_label.grid(row=2, column=2, sticky=sticky, padx=padx, pady=pady)
        self.city_entry = tkinter.Label(user_info_frame, text="Teplice", width=width2)
        #self.city_entry = tkinter.Entry(user_info_frame)
        self.city_entry.grid(row=2, column=3, sticky=sticky2, padx=padx, pady=pady)

        # vytvoření popisku a zadávacího pole pro PSČ
        zip_label = tkinter.Label(user_info_frame, text="Psč:", width=width)
        zip_label.grid(row=2, column=4, sticky=sticky, padx=padx, pady=pady)
        self.zip_entry = tkinter.Label(user_info_frame, text="415 01", width=width2)
        #self.zip_entry = tkinter.Entry(user_info_frame)
        self.zip_entry.grid(row=2, column=5, sticky=sticky2, padx=padx, pady=pady)


        # vytvoření rámu pro nabídku možností
        user_info_frame_offer = tkinter.LabelFrame(self._frame, text="Možnosti")
        # umístnění rámu pro vyhledávací okno v rodičovském rámu
        user_info_frame_offer.grid(row=1, column=0, sticky="ew", padx=0, pady=5)
        # lokální proměnná pro šířku tlačítka
        width = 14

        # vytvoření a umístění tlačítka pro editaci
        search_button = tkinter.Button(user_info_frame_offer, text="Sjednaná pojištění", width=width)
        search_button.grid(row=0, column=0, sticky="news", padx=12, pady=5)
        # vytvoření a umístění tlačítka pro editaci
        search_button = tkinter.Button(user_info_frame_offer, text="Nové pojištění", width=width)
        search_button.grid(row=0, column=1, sticky="news", padx=12, pady=5)
        # vytvoření a umístění tlačítka pro vyhledání výsledku
        search_button = tkinter.Button(user_info_frame_offer, text="Upravit záznam", width=width)
        search_button.grid(row=0, column=2, sticky="news", padx=12, pady=5)
        # vytvoření a umístění tlačítka pro vyhledání výsledku
        search_button = tkinter.Button(user_info_frame_offer, text="Smazat záznam", width=width)
        search_button.grid(row=0, column=3, sticky="news", padx=12, pady=5)
        # vytvoření a umístění tlačítka pro vyhledání výsledku
        search_button = tkinter.Button(user_info_frame_offer, text="Zpět", width=width)
        search_button.grid(row=0, column=4, sticky="news", padx=12, pady=5)










