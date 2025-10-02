import pandas as pd
from sqlalchemy import create_engine

def csv_to_sqlite(csv_file, db_path, table='data'):
    df = pd.read_csv(csv_file)
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql(table, engine, if_exists='replace', index=False)
    return "converted"

def sqlite_to_csv(db_path, csv_file, table='data'):
    engine = create_engine(f"sqlite:///{db_path}")
    df = pd.read_sql(f"SELECT * FROM {table}", engine)
    df.to_csv(csv_file, index=False)
    return "converted"

def excel_to_csv(xl_file, csv_file, sheet_name='Sheet1'):
    df = pd.read_excel(xl_file, sheet_name=sheet_name)
    df.to_csv(csv_file, index=False)
    return "converted"

def csv_to_excel(csv_file, xl_file):
    df = pd.read_csv(csv_file)
    df.to_excel(xl_file, index=False)
    return "converted"
