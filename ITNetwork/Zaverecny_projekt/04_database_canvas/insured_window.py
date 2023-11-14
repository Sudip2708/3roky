import tkinter
from tkinter import ttk
from next_window import NextWindow
import db

class InsuredWindow:

    def __init__(self, window_name, window_size):
        # vytvoření základního okna
        root_window = tkinter.Tk()
        root_window.title(window_name)
        root_window.geometry(window_size)
        # přidání stylu (k tabulce)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading', background="light gray")
        # vytvoření základního rámu
        self._frame = tkinter.Frame(root_window)
        self._frame.pack()
        # vytvoření pole pro hledání
        self.create_search_entry()
        # vytvoření pole pro výsledky hledání
        self.create_table()
        # vytvoření pole pro něco dalšího
        # self.create_next_field()
        # smyčka hlavního okna
        root_window.mainloop()

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
        # vytvoření rámu pro vyhledávací okno
        user_search_frame = tkinter.LabelFrame(self._frame, text="Hledání pojištěnce")
        # umístnění rámu pro vyhledávací okno v rodičovském rámu
        user_search_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=5)
        # lokální proměnné pro spadávky a umístění
        padx = 14
        pady = 5
        sticky = "we"
        # vytvoření a umístění tlačítka pro vyhledání výsledku
        search_button = tkinter.Button(user_search_frame, text="HLEDAT", command=self.get_search_data)
        search_button.grid(row=0, rowspan=2, column=5, sticky="news", padx=12, pady=5)
        # vytvoření popisku a zadávacího pole pro jméno
        name_label = tkinter.Label(user_search_frame, text="Jméno")
        name_label.grid(row=0, column=0, sticky=sticky, padx=padx, pady=pady)
        self.name_entry = tkinter.Entry(user_search_frame)
        self.name_entry.grid(row=0, column=1, sticky=sticky, padx=padx, pady=pady)
        # vytvoření popisku a zadávacího pole pro příjmení
        surname_label = tkinter.Label(user_search_frame, text="Příjmení")
        surname_label.grid(row=0, column=2, sticky=sticky, padx=padx, pady=pady)
        self.surname_entry = tkinter.Entry(user_search_frame)
        self.surname_entry.grid(row=0, column=3, sticky=sticky, padx=padx, pady=pady)
        # vytvoření popisku a zadávacího pole pro email
        email_label = tkinter.Label(user_search_frame, text="Email")
        email_label.grid(row=1, column=0, sticky=sticky, padx=padx, pady=pady)
        self.email_entry = tkinter.Entry(user_search_frame)
        self.email_entry.grid(row=1, column=1, sticky=sticky, padx=padx, pady=pady)
        # vytvoření popisku a zadávacího pole pro telefon
        phone_label = tkinter.Label(user_search_frame, text="Telefon")
        phone_label.grid(row=1, column=2, sticky=sticky, padx=padx, pady=pady)
        self.phone_entry = tkinter.Entry(user_search_frame)
        self.phone_entry.grid(row=1, column=3, sticky=sticky, padx=padx, pady=pady)
        # vytvoření popisku a zadávacího pole pro adresu
        address_label = tkinter.Label(user_search_frame, text="Adresa")
        address_label.grid(row=2, column=0, sticky=sticky, padx=padx, pady=pady)
        self.address_entry = tkinter.Entry(user_search_frame)
        self.address_entry.grid(row=2, column=1, sticky=sticky, padx=padx, pady=pady)
        # vytvoření popisku a zadávacího pole pro město
        city_label = tkinter.Label(user_search_frame, text="Město")
        city_label.grid(row=2, column=2, sticky=sticky, padx=padx, pady=pady)
        self.city_entry = tkinter.Entry(user_search_frame)
        self.city_entry.grid(row=2, column=3, sticky=sticky, padx=padx, pady=pady)
        # vytvoření popisku a zadávacího pole pro PSČ
        zip_label = tkinter.Label(user_search_frame, text="Psč")
        zip_label.grid(row=2, column=4, sticky=sticky, padx=padx, pady=pady)
        self.zip_entry = tkinter.Entry(user_search_frame)
        self.zip_entry.grid(row=2, column=5, sticky=sticky, padx=padx, pady=pady)
        # vytvoření oznamu o použití %
        instructions_text = "Znak % umístěný na začátku hledaného výrazu hledá výskyt výrazu v celém textu."
        instructions_label = tkinter.Label(user_search_frame, text=instructions_text, font='Arial 8',
                                           foreground='white', background='light grey')
        instructions_label.grid(row=3, column=0, columnspan=6, sticky="we", padx=padx, pady=pady)


    def create_table(self):
        # vytvoření rámu tabulky
        table_frame = tkinter.LabelFrame(self._frame, text="Výsledky")
        # umístnění rámu tabulky v rodičovském rámu
        table_frame.grid(row=2, column=0, sticky="news", padx=0, pady=0)
        # názvy všech sloupců
        columns_name = ('id', 'name', 'surname', 'email', 'phone', 'address', 'city', 'zip')
        # sloupce, které budou zobrazeny
        displaycolumns = ('name', 'surname', 'address', 'city', 'zip')
        # vytvoření tabulky
        self._tree = ttk.Treeview(table_frame, columns=columns_name, height=10,
                                  show='headings', selectmode='browse', displaycolumns=displaycolumns)
        # umístění tabulky do místního rámu
        self._tree.grid(row=0, column=1, sticky="news", padx=0, pady=5)
        # nastavení pro nadpisy sloupců
        self._tree.heading('id', text='ID', anchor='w')
        self._tree.heading('name', text='Jméno', anchor='w')
        self._tree.heading('surname', text='Příjmení', anchor='w')
        self._tree.heading('email', text='Email', anchor='w')
        self._tree.heading('phone', text='Telefon', anchor='w')
        self._tree.heading('address', text='Adresa', anchor='w')
        self._tree.heading('city', text='Město', anchor='w')
        self._tree.heading('zip', text='PSČ', anchor='w')
        # nastavení sloupců
        self._tree.column('id', anchor='w', width=30)
        self._tree.column('name', anchor='w', width=120)
        self._tree.column('surname', anchor='w', width=120)
        self._tree.column('email', anchor='w', width=150)
        self._tree.column('phone', anchor='w', width=120)
        self._tree.column('address', anchor='w', width=200)
        self._tree.column('city', anchor='w', width=120)
        self._tree.column('zip', anchor='w', width=70)
        # přidání rolovací lišty
        yscrollbar = ttk.Scrollbar(table_frame, orient=tkinter.VERTICAL, command=self._tree.yview)
        self._tree.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.grid(row=0, column=2, sticky='news', padx=0, pady=5)
        # přidání vycpávky před začátek tabulky (aby nebyla tolik nakraji)
        label = tkinter.Label(table_frame,)
        label.grid(row=0, column=0, sticky='news')
        self._tree.bind('<<TreeviewSelect>>', self.item_selected)

    def item_selected(self, event):
        for selected_item in self._tree.selection():
            item = self._tree.item(selected_item)
            print(item)
            record = item['values']
            print(record)
            window_name = "Detail pojištěnce"
            window_size = '700x500'
            NextWindow(window_name, window_size)
            # show a message
            #showinfo(title='Information', message=','.join(record))

    def update_table(self):
        # smazání obsahu tabulky
        self._tree.delete(*self._tree.get_children())
        # vložení dat (z atributu _table_content)
        for contact in self._table_content:
            self._tree.insert('', tkinter.END, values=contact)

    # def create_next_field(self):
    #     search_button = tkinter.Button(self._frame, text="VYBRAT")
    #     search_button.grid(row=3, column=0, sticky="news", padx=12, pady=5)






