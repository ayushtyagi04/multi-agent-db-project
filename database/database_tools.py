import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import shutil
import os

def upload_file(source_path, dest_folder="data"):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    filename = os.path.basename(source_path)
    dest_path = os.path.join(dest_folder, filename)
    shutil.copy(source_path, dest_path)
    return dest_path

# CSV Operations
def csv_delete_rows(csv_file, column, value):
    df = pd.read_csv(csv_file)
    df = df[df[column] != value]
    df.to_csv(csv_file, index=False)
    return "deleted"

def csv_add_column(csv_file, column, default=None):
    df = pd.read_csv(csv_file)
    df[column] = default
    df.to_csv(csv_file, index=False)
    return "added"

def csv_update_rows(csv_file, column, new_value, condition_column, condition_value):
    df = pd.read_csv(csv_file)
    cond_mask = df[condition_column].fillna('') == condition_value
    df.loc[cond_mask, column] = new_value
    df.to_csv(csv_file, index=False)
    return "updated"

def csv_read_rows(csv_file, condition_column=None, condition_value=None):
    df = pd.read_csv(csv_file)
    if condition_column and condition_value:
        df = df[df[condition_column] == condition_value]
    return df.to_dict(orient="records")

# SQLite Operations
def sqlite_delete_rows(db_path, table, column, value):
    engine = create_engine(f"sqlite:///{db_path}")
    query = f"DELETE FROM {table} WHERE {column}='{value}'"
    with engine.connect() as conn:
        conn.execute(query)
    return "deleted"

def sqlite_add_column(db_path, table, column, coltype="TEXT"):
    engine = create_engine(f"sqlite:///{db_path}")
    query = f"ALTER TABLE {table} ADD COLUMN {column} {coltype}"
    with engine.connect() as conn:
        conn.execute(query)
    return "added"

def sqlite_update_rows(db_path, table, column, new_value, condition_column, condition_value):
    engine = create_engine(f"sqlite:///{db_path}")
    query = f"UPDATE {table} SET {column}='{new_value}' WHERE {condition_column}='{condition_value}'"
    with engine.connect() as conn:
        conn.execute(query)
    return "updated"

def sqlite_read_rows(db_path, table, condition_column=None, condition_value=None):
    engine = create_engine(f"sqlite:///{db_path}")
    query = f"SELECT * FROM {table}"
    if condition_column and condition_value:
        query += f" WHERE {condition_column}='{condition_value}'"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

# SQL Server Operations
def sql_delete_rows(conn_str, table, column, value):
    engine = create_engine(conn_str)
    query = f"DELETE FROM {table} WHERE {column}='{value}'"
    with engine.connect() as conn:
        conn.execute(query)
    return "deleted"

def sql_add_column(conn_str, table, column, coltype="VARCHAR(255)"):
    engine = create_engine(conn_str)
    query = f"ALTER TABLE {table} ADD {column} {coltype}"
    with engine.connect() as conn:
        conn.execute(query)
    return "added"

def sql_update_rows(conn_str, table, column, new_value, condition_column, condition_value):
    engine = create_engine(conn_str)
    query = f"UPDATE {table} SET {column}='{new_value}' WHERE {condition_column}='{condition_value}'"
    with engine.connect() as conn:
        conn.execute(query)
    return "updated"

def sql_read_rows(conn_str, table, condition_column=None, condition_value=None):
    engine = create_engine(conn_str)
    query = f"SELECT * FROM {table}"
    if condition_column and condition_value:
        query += f" WHERE {condition_column}='{condition_value}'"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

# Excel Operations
def excel_delete_rows(xl_file, sheet, column, value):
    df = pd.read_excel(xl_file, sheet_name=sheet)
    df = df[df[column] != value]
    df.to_excel(xl_file, sheet_name=sheet, index=False)
    return "deleted"

def excel_add_column(xl_file, sheet, column, default=None):
    df = pd.read_excel(xl_file, sheet_name=sheet)
    df[column] = default
    df.to_excel(xl_file, sheet_name=sheet, index=False)
    return "added"

def excel_update_rows(xl_file, sheet, column, new_value, condition_column, condition_value):
    df = pd.read_excel(xl_file, sheet_name=sheet)
    cond_mask = df[condition_column].fillna('') == condition_value
    df.loc[cond_mask, column] = new_value
    df.to_excel(xl_file, sheet_name=sheet, index=False)
    return "updated"

def excel_read_rows(xl_file, sheet, condition_column=None, condition_value=None):
    df = pd.read_excel(xl_file, sheet_name=sheet)
    if condition_column and condition_value:
        df = df[df[condition_column] == condition_value]
    return df.to_dict(orient="records")
