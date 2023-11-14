import sqlite3

def create_database_table(database, table, values):
    """
    Funkce vytvoří tabulku v databázy (případně i databázy, neníli ještě vytvořená)
    :param database: Název databáze (i s koncovkou db)
    :param table: Název tabulky kterou chceme vytvořit
    :param values: Názvy sloupců (v jednoduchých uvozovkách) a DATATYPE, oddělených čárkou a uložených v TUPLE
    :return: NONE + info_text
    """
    conn = sqlite3.connect(f"{database}")
    c = conn.cursor()
    command_query = f"CREATE TABLE {table} ({values})"
    c.execute(command_query)
    conn.commit()
    conn.close()
    print(f"Byla vytvořena tabulka '{table}' databáze '{database}', s hodnotami sloupců:\n{values}\n")
"""
    Připoj se k databázy a vytvoř proměnou 'conn' pro navázané spojení
    Vytvoř proměnou 'c' pro kurzor
    Vytvoř proměnnou 'command_query' pro text SQL příkazu
    Proveď dotaz vytvoření tabulky a přidání sloupců (sloupec s ID se generuje automaticky)
    Ulož změny
    Ukonči spojení
    Vypiš oznam o úspěšném provedení
    """

# def create_database_in_memory(database, table, values):
#     conn = sqlite3.connect(':memory:')
#     c = conn.cursor()
#     c.execute(f"CREATE TABLE {table} {values})
#     pass

def add_one_row(database, table, values):
    """
    Funkce přidá jeden řádek do tabulky databáze
    :param database: název databáze (i s koncovkou db)
    :param table: název tabulky do které chceme přidávat data
    :param values: TUPLE s vkládanými hodnotami v pořadí dle sloupců v tabulce
    :return: NONE + info_text
    """
    conn = sqlite3.connect(f"{database}")
    c = conn.cursor()
    question_marks = ("?," * len(values))[0:-1]
    command_query = f"INSERT INTO {table} VALUES ("+question_marks+")"
    c.execute(command_query, values)
    conn.commit()
    conn.close()
    print(f"Do tabulky '{table}' databáze '{database}', byl přidán záznam:\n{values}\n")
"""
    Připoj se k databázy a vytvoř proměnou 'conn' pro navázané spojení
    Vytvoř proměnou 'c' pro kurzor
    Dle počtu položek 'values'', vytvoř zástuponé otazníky a přidej je do proměnné 'question_marks'
    Vytvoř proměnnou 'command_query' pro text SQL příkazu
    Proveď příkaz na přidání hodnot do tabulky
    Ulož změny
    Ukonči spojení
    Vypiš oznam o úspěšném provedení
    """

def add_multiple_rows(database, table, values):
    """
    Funkce přidá více řádků do tabulky databáze
    :param database: název databáze (i s koncovkou db)
    :param table: název tabulky do které chceme přidávat data
    :param values:  LIST of TUPLES (pro jednotlivé řádky) s vkládanými hodnotami v pořadí dle sloupců v tabulce
    :return: NONE + info_text
    """
    conn = sqlite3.connect(f"{database}")
    c = conn.cursor()
    question_marks = ("?," * len(values[0]))[0:-1]
    command_query = f"INSERT INTO {table} VALUES (" + question_marks + ")"
    c.executemany(command_query, values)
    conn.commit()
    conn.close()
    print(f"Do tabulky '{table}' databáze '{database}', byl přidán záznam:\n{values}\n")
"""
    Připoj se k databázy a vytvoř proměnou 'conn' pro navázané spojení
    Vytvoř proměnou 'c' pro kurzor
    Dle počtu položek 'values'', vytvoř zástuponé otazníky a přidej je do proměnné 'question_marks'
    Vytvoř proměnnou 'command_query' pro text SQL příkazu
    Proveď příkaz na přidání hodnot do tabulky
    Ulož změny
    Ukonči spojení
    Vypiš oznam o úspěšném provedení
    """

def get_all_rows(database, table):
    """
    Funkce načte a vrátí veškerý obsah tabulky databáze
    :param database: Název databáze (i s koncovkou db)
    :param table: Název tabulky kterou chceme zobrazit
    :return: Obsah tabulky databáze kde jednotlivé řádky jsou uložené jako TUPLE
    """
    conn = sqlite3.connect(f"{database}")
    c = conn.cursor()
    command_query = f"SELECT rowid, * FROM {table}"
    c.execute(command_query)
    database_content = c.fetchall()
    conn.close()
    return database_content
"""
    Připoj se k databázy a vytvoř proměnou 'conn' pro navázané spojení
    Vytvoř proměnou 'c' pro kurzor
    Vytvoř proměnnou 'command_query' pro text SQL příkazu
    Proveď dotaz na výběr všech sluopců a řádků z tabulky databáze
    Přiřaď všechny záznamy do proměnné 'database_content'
    Ukonči spojení
    Vrať obsah proměnné 'database_content'
    """

def show_id_row(database, table, row_id):
    """
    Funkce načte a vrátí veškerý obsah tabulky databáze
    :param database: Název databáze (i s koncovkou db)
    :param table: Název tabulky kterou chceme zobrazit
    :return: Obsah tabulky databáze kde jednotlivé řádky jsou uložené jako TUPLE
    """
    conn = sqlite3.connect(f"{database}")
    c = conn.cursor()
    command_query = f"SELECT rowid, * FROM {table} WHERE rowid = (?)"
    c.execute(command_query, str(row_id))
    database_content = c.fetchone()
    conn.close()
    return database_content
"""
    Připoj se k databázy a vytvoř proměnou 'conn' pro navázané spojení
    Vytvoř proměnou 'c' pro kurzor
    Vytvoř proměnnou 'command_query' pro text SQL příkazu
    Proveď dotaz na výběr všech sloupců pro konkrétní řádek z tabulky databáze
    Přiřaď všechny záznamy do proměnné 'database_content'
    Ukonči spojení
    Vrať obsah proměnné 'database_content'
    """
#
# def show_multiple_row(database, table, what, value):
#
# def delete_one(database, table, values):
#     """
#     Funkce přidá jednu položku do databáze
#     :param database: název databáze (i s koncovkou db)
#     :param table: název tabulky do které chceme přidávat data
#     :param values: názvi sloupců tabulky (uložené jako TUPLE)
#     :return: NONE + info_text
#     """
#     conn = sqlite3.connect(f"{database, table, row_id}")
#     c = conn.cursor()
#     row_id = int(row_id)
#     delete_row = c.execute(f"SELECT rowid, * FROM {table} WHERE rowid = (?)", row_id)
#     c.execute(f"DELETE from {table} WHERE rowid = (?)", row_id)
#     conn.commit()
#     conn.close()
#     print(f"Z tabulky '{table}' databáze '{database}', byl odstraněn záznam:\n{delete_row}\n")
# """
#     Připoj se k databázy a vytvoř proměnou 'conn' pro navázané spojení
#     Vytvoř proměnou 'c' pro kurzor
#     Dle počtu položek přidávaných hodnot, vytvoř zástuponé otazníky a přidej je do proměnné
#     Proveď příkaz na smazání řádku z tabulky databáze
#     Ulož změny
#     Ukonči spojení
#     Vypiš oznam o úspěšném provedení
#     """