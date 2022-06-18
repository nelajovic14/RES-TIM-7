
from distutils.log import error
from msilib.schema import Error
from sqlite3 import DatabaseError
import cx_Oracle
from email import message

class Baza:
    def __init__(self,c) :
        self.connection = cx_Oracle.connect(c)
    def do_query(self,query):
        cur=self.connection.cursor()
        try:
            cur.execute(query)
            self.connection.commit()
        except cx_Oracle.DatabaseError:
            raise cx_Oracle.DatabaseError("Database")
    def do_query_with_result(self,query):
        cur=self.connection.cursor()
        try:
            cur.execute(query)
            result=cur.fetchall()
            return result
        except cx_Oracle.DatabaseError:
            raise cx_Oracle.DatabaseError("Database")
