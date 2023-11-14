import sqlite3

def get_table_data(database, table_name, colomns_names="*", row_condition=None, order_instruction=None, output_limit=None):



    command_query = f"SELECT {colomns_names} FROM {table_name} "
    if row_condition:
        command_query += f"WHERE {row_condition} "
    if order_instruction:
        command_query += f"ORDER BY {order_instruction} "
    if output_limit:
        command_query += f"LIMIT {output_limit} "
    command_query += ";"

    print(command_query)



    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(command_query)
    database_content = cur.fetchall()
    conn.close()
    return database_content

