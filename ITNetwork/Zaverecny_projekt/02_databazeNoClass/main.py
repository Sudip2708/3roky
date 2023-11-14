import db

# Vytvoření databáze
# database = 'prvni_databaze.db'
# table = 'prvni_tabulka'
# values = 'firs_name TEXT, last_name TEXT, email TEXT, phone TEXT, age INTEGER'
# db.create_database_table(database, table, values)
"""
Název tabulky databáze
Název tabulky
Názvy sloupců + DATATYP:
    NULL = nemá hodnotu v databázi
    INTEGER = celá čísla
    REAL = čísla s desetinou čárkou
    TEXT = text
    BLOB = audiovyzuální obsah
Volání funkce na vytvoření tabulky
"""

# Přidání jednoho řádku do databáze
# database = 'prvni_databaze.db'
# table = 'prvni_tabulka'
# values = ('Dalibor', 'Sova', 'dalibor@sova.cz', '+420704564595', 47)
# db.add_one_row(database, table, values)
"""
Název tabulky databáze
Název tabulky
Hodnoty pro přidání (musí korespondovat s pořadím sloupců a jejich DATATYPem)
Volání funkce na vložení záznamu
"""

# Přidání více řádků do databáze
# database = 'prvni_databaze.db'
# table = 'prvni_tabulka'
# values = [
#     ('Petr', 'Pavel', 'petr@paVEL.cz', '+420795389652', 69),
#     ('Kamila', 'Rambousková', 'kamila@rambouskova.cz', '+420852963741', 36),
#     ('František', 'Nesvačil', 'frantisek@nesvacil.cz', '+420159753258', 47),
#     ('Tomáš', 'Marný', 'tomas@marny.cz', '+420456123789', 47),
#     ('Alžběta', 'Frýšová', 'alzbeta@frysova.cz', '+420753421869', 47),
#     ]
# db.add_multiple_rows(database, table, values)
"""
Název tabulky databáze
Název tabulky
Seznam hodnot (LIST) pro přidání hodnot (TUPLE)do databáze (musí korespondovat s pořadím sloupců a jejich DATATYPem)
Volání funkce na vložení záznamu
"""

# Vrať obsah celé tabulky
# database = 'prvni_databaze.db'
# table = 'prvni_tabulka'
# database_content = db.get_all_rows(database, table)
# for tuple in database_content:
#     print(tuple)
"""
Název tabulky databáze
Název tabulky
Volání funkce pro vytažení všech záznamů databáze a uložení do proměnné 'database_content'
Cyklus pro jednotlivé řádky (TUPLE) uvnitř seznamu (LIST) s obsahem databáze
    Výpis řádku (TUPLE)
"""

# Vrať řádek dle generovaného ID (rowid)
# database = 'prvni_databaze.db'
# table = 'prvni_tabulka'
# row_id = 5
# database_content = db.show_id_row(database, table, row_id)
# print(database_content)
"""
Název tabulky databáze 
Název tabulky 
Generované ID řádku (v tabulce vytvořené v Pythonu)
Volání funkce pro vytažení záznamu z databáze a uložení do proměnné 'database_content'
Výpis řádku (TUPLE)
"""