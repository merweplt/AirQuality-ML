import pandas as pd
from sqlalchemy import create_engine

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def save_data(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)
        print(f"✅ Veriler '{table_name}' tablosuna kaydedildi.")

    def load_data(self, query):
        return pd.read_sql(query, self.engine)