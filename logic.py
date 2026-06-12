from flask import request
from sqlalchemy import create_engine
import pandas as pd
import model
import psycopg2
import db
import os

class LogicException(Exception):
    pass

class DBLogic():

    def __init__(self):
        self._file_db = db.FileDB()
        self.data = ""
        self.file = model.DF()
        self.path = None
        self.result = None

    def get_conn(self):
        try:
            self.conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="1234",
                host="localhost",
                port="5432"
            )
            print("Подключение успешно!")

            self.cur = self.conn.cursor()

            self.cur.execute("SELECT version();")
            self.db_version = self.cur.fetchone()
            print(f"Версия PostgreSQL: {self.db_version}")
            self.conn.commit()
        except Exception as ex:
            raise LogicException(ex)
        finally:
            if self.conn is not None:
                self.conn.close()

    def upload_db(self):
        try:
            self.data = str(request.get_data(), encoding='utf-8')
            self.file = model.DF()
            self.file.filename = self.data
            self.file.filepath = os.path.abspath(self.data)
            self.file.result_of_analysis = ''
            self.path = self.file.filepath
            print(self.data)
            self.DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"
            self.engine = create_engine(self.DATABASE_URL)
            if self.data.endswith(".csv"):
                self.db = pd.read_csv(self.data)
            elif self.data.endswith(".xlsx"):
                self.db = pd.read_excel(self.data)
            self.db.to_sql('file_1', self.engine, if_exists='replace', index=False)
            print(f" Файл {self.data} загружен в базу. Путь:{self.file.filepath} ")
        except Exception as ex:
            raise LogicException(ex)

    def list_db(self):
        try:
            if self.data.endswith(".csv"):
                self.db = pd.read_csv(self.data)
            elif self.data.endswith(".xlsx"):
                self.db = pd.read_excel(self.data)
            print(f" Данные таблицы: {self.db.head(15)}")
        except Exception as ex:
            raise LogicException(ex)

    def get_stats(self):
        try:
            if self.data.endswith(".csv"):
                self.db = pd.read_csv(self.data)
            elif self.data.endswith(".xlsx"):
                self.db = pd.read_excel(self.data)
            print(self.db.head())
            self.mean_values = self.db.mean(numeric_only=True)
            self.median_values = self.db.median(numeric_only=True)
            self.correlation = self.db.corr(numeric_only=True)
            self.result = f"Среднее значение по столбцам: {self.mean_values}, Медианное значение: {self.median_values}, Корреляция: {self.correlation}"
            print(self.result)
        except Exception as ex:
            raise LogicException(ex)

    def clean_data(self):
        try:
            if self.data.endswith(".csv"):
                self.db = pd.read_csv(self.data)
            elif self.data.endswith(".xlsx"):
                self.db = pd.read_excel(self.data)
            self.db_cleared = self.db.drop_duplicates()
            self.db_ = self.db_cleared.fillna('No information')
            self.DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"
            self.engine = create_engine(self.DATABASE_URL)
            self.db_.to_sql('file_cleared', self.engine, if_exists='replace', index=False)
        except Exception as ex:
            raise LogicException(ex)