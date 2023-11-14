import sqlite3

class Database:


    _list_of_databases = []

    # _instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(Database)
    #         return cls._instance
    #     return cls._instance


    def __init__(db, database_name):
        db._name = database_name
        db._conn = sqlite3.connect(database_name)
        db._cur = db._conn.cursor()
        db._list_of_databases.append(db._name)


    def __str__(db):
        return _database_name


    def __del__(db):
        db._cur.close()
        db._conn.close()


    def create_table(db, table_name, colomns_name_velues):
        command_query = f"CREATE TABLE IF NOT EXISTS {table_name} {colomns_name_velues};"
        db._cur.execute(command_query)
        return f"""
        V databázi {db._name},
        byla vytvořena tabulka {table_name},
        s hodnotami: {colomns_name_velues}"""


    def delete_table(db, table_name):
        command_query = f"DROP TABLE {table_name};"
        db._cur.execute(command_query)
        return f"""
        Z databáze {db._name}, 
        byla odstraněna tabulka {table_name}"""


    def alter_table(db, table_name,
                    new_table_name = None,
                    old_column_name = None,
                    new_column_name = None,
                    add_column = None,
                    delete_column = None
                    ):
        command_query = f"ALTER TABLE {table_name} "
        output_text = ""
        if new_table_name:
            command_query += f"RENAME TO {new_table_name}"
            output_text = f"byla přejmenovaná tabulka {table_name} na {new_table_name}"
        elif old_column_name and new_column_name:
            command_query += f"RENAME TO {old_column_name} TO {new_column_name}"
            output_text = f"byl změněn název sloupce {old_column_name} na {new_column_name}"
        elif add_column:
            command_query += f"ADD {add_column}"
            output_text = f"byl přidán nový sloupec {add_column}"
        elif delete_column:
            command_query += f"DROP {add_column}"
            output_text = f"byl odstraněn sloupec {delete_column}"
        db._cur.execute(command_query)
        return f"V tabulce {table_name} databáze {db._name} " + output_text


    def get_table_data(db, table_name,
                       colomns_names = "*",
                       row_condition = None,
                       order_instruction = None,
                       output_limit = None
                       ):
        command_query = f"SELECT {colomns_names} FROM {table_name} "
        if row_condition:
            command_query += f"WHERE {row_condition} "
        if order_instruction:
            command_query += f"ORDER BY {order_instruction} "
        if output_limit:
            command_query += f"LIMIT {output_limit} "
        db._cur.execute(command_query)
        database_content = db._cur.fetchall()
        return database_content


    def get_column_names(db, table_name):
        command_query = f"SELECT * FROM {table_name}"
        db._cur.execute(command_query)
        recieved_data = db._cur.description
        column_names = []
        for one_tuple in recieved_data:
            column_names.append(one_tuple[0])
        return column_names


    def add_data_into_table(db, table_name, column_names, row_values):
        #number_of_items = len(row_values)
        #question_marks = ("?," * number_of_items)[0:-1]
        #command_query = f"INSERT INTO {table_name} {column_names} VALUES ({question_marks})"
        #db._cur.execute(command_query, row_values)
        command_query = f"INSERT INTO {table_name} {column_names} VALUES {row_values};"
        db._cur.execute(command_query)
        db._conn.commit()
        return f"""Do tabulky '{table_name}' databáze '{db._name}'
        byli přidány do kolonek: {column_names}
        data:{row_values}"""



    def change_table_data(db, table_name, colomn_names_and_velues, condition=None):
        command_query = f"UPDATE {table_name} SET {colomn_names_and_velues} "
        if condition:
            command_query += f"WHERE {condition} "
        db._cur.execute(command_query)
        if condition:
            return f"""V tabulce '{table_name}' databáze '{db._name}'
            byli změněny na základě podmínky: {condition}
            následující data:{colomn_names_and_velues}"""
        else:
            return f"""V tabulce '{table_name}' databáze '{db._name}'
            následující data:{colomn_names_and_velues}"""


    def delete_one_row_from_table(db, table_name, condition):
        command_query = f"DELETE FROM {table_name} WHERE {condition} "
        db._cur.execute(command_query)
        return f"""Z tabulky {table_name} databáze {db._name} 
        byl odebrán řádek (nebo řádky) dle podmínky: {condition}"""


    def delete_all_table_content(db, table_name):
        command_query = f"DELETE FROM {table_name}"
        db._cur.execute(command_query)
        return f"""Z tabulky {table_name} databáze {db._name} 
        byla smazaná všechna data"""


    def get_multiple_table_data(db, colomns_names, main_table, tables_to_join, colomns_id_matching):
        join_query = ""
        number_of_tables = len(tables_to_join)
        for i in range(number_of_tables):
            table = tables_to_join[i]
            id_match = colomns_id_matching[i]
            join_query += f"JOIN {table} ON {id_match} "
        command_query = f"SELECT {colomns_names} FROM {main_table} " + join_query
        db._cur.execute(command_query)
        database_content = db._cur.fetchall()
        return database_content


    def get_table_data(db, table_name,
                       colomns_names = "*",
                       row_condition = None,
                       order_instruction = None,
                       output_limit = None
                       ):
        command_query = f"SELECT {colomns_names} FROM {table_name} "
        if row_condition:
            command_query += f"WHERE {row_condition} "
        if order_instruction:
            command_query += f"ORDER BY {order_instruction} "
        if output_limit:
            command_query += f"LIMIT {output_limit} "
        db._cur.execute(command_query)
        database_content = db._cur.fetchall()
        return database_content