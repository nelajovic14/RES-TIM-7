from distutils.log import error
from msilib.schema import Error
import cx_Oracle
from email import message

class Baza:
    def __init__(self,c) :
        self.connection = cx_Oracle.connect(c)
        print(c)
    def do_query(self,query):
        cur=self.connection.cursor()
        try:
            cur.execute(query)
            self.connection.commit()
        except Exception:
            raise Error("Nije moguce upisati podatke u bazu")
