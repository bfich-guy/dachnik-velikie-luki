from aiosqlite import connect, Cursor

from typing import Any


#region CRUD: Create

async def create_database_table(
    *, 
    file_path: str, 
    table_name: str, 
    columns_list: list[str],
) -> None:
    
    async with connect(file_path) as db:
        columns_list_is_empty: bool = not columns_list

        if columns_list_is_empty:
            return

        columns: str = ", ".join(columns_list)
        database_query: str = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"

        await db.execute(database_query)
        await db.commit()


async def create_database_column(
    *, 
    file_path: str, 
    table_name: str, 
    column: str,
) -> None:
    
    async with connect(file_path) as db:
        column_is_empty: bool = not column
        
        if column_is_empty:
            return
        
        database_query: str = f"ALTER TABLE {table_name} ADD COLUMN {column};"
        await db.execute(database_query)
        await db.commit()

#endregion


#region CRUD: Read

async def read_database_table(
    *, 
    file_path: str,
    table_name: str,
    condition: str | None = None,
    params: tuple | None = None,
) -> list[tuple]:

    database_query: str = f"SELECT * FROM {table_name};" if condition is None else f"SELECT * FROM {table_name} WHERE {condition};"

    async with connect(file_path) as db:
        cursor: Cursor = await db.execute(database_query, params or ())
        data: list[tuple] = await cursor.fetchall()
        return data


async def read_database_column(
    *, 
    file_path: str,
    table_name: str,
    column: str,
    condition: str | None = None,
    params: tuple | None = None,
) -> list[Any]:

    database_query: str = f"SELECT {column} FROM {table_name};" if condition is None else f"SELECT {column} FROM {table_name} WHERE {condition};"

    async with connect(file_path) as db:
        cursor: Cursor = await db.execute(database_query, params or ())
        data: list[Any] = [data[0] for data in await cursor.fetchall()]
        return data

#endregion
