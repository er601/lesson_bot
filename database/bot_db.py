import sqlite3
from config import bot


def sql_create():
    global connection, cursor
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    if connection:
        print("Database connected successfully")
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS tvshow
    (photo TEXT, title TEXT PRIMARY KEY, description TEXT) 
    '''
    connection.execute(
        create_table_query
    )
    connection.commit()


async def sql_insert(state):
    async with state.proxy() as data:
        cursor.execute('''
        INSERT INTO tvshow VALUES (?, ?, ?)
        ''', tuple(data.values()))
        connection.commit()


async def sql_select(message):
    for result in cursor.execute('''SELECT * FROM tvshow''').fetchall():
        await bot.send_photo(message.chat.id,
                             result[0],
                             caption=f'Title: {result[1]}\n'
                                     f'Description: {result[2]}')


async def sql_select_for_delete():
    return cursor.execute('''SELECT * FROM tvshow''').fetchall()


async def sql_delete(data):
    cursor.execute('''
    DELETE FROM tvshow WHERE title == ?
    ''', (data,))
    connection.commit()
