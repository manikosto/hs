

from email.header import Header
import pytest
import os
# import cx_Oracle
import sqlite3
# from dateutil.relativedelta import *
from libs.helper import Helper


# Oracle connection
# cx_Oracle.init_oracle_client(lib_dir="/usr/lib/oracle/19.13/client64/lib") # Docker connection
# cx_Oracle.init_oracle_client(lib_dir="/Users/manikosto/Downloads/oracle") # Local connection



class DbRequest:

    if os.environ['DB'] == 'sqlite':
        def __enter__(self):
            connection = sqlite3.connect(os.getcwd() + '/db/users.db')
            self.connection = connection
            print(self.connection)
            return self

        def __exit__(self, a, b, c):
            self.connection.close()
            # print(self.connection)
    
    # elif os.environ['DB'] == 'oracle':
        
    #     def __enter__(self):
    #         dsn = cx_Oracle.makedsn(
    #             'lgb3-db.int', 
    #             '1522', 
    #             service_name='fcc'
    #             )
    #         connection = cx_Oracle.connect(
    #             user='FCCUSER', 
    #             password='fccuser', 
    #             dsn=dsn
    #         )
    #         self.connection = connection
    #         # print(self.connection)
    #         return self

    #     def __exit__(self, a, b, c):
    #         self.connection.close()
    #         # print(self.connection)
        
    elif os.environ['DB'] == "x":
        pass

    def get_users(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM users")
        res = self.cursor.fetchall()
        return str(res)
        

    # def select_subscription_by_email(self, email):
    #     self.cursor = self.connection.cursor()
    #     self.cursor.execute(f"SELECT * FROM FCC2.SUBSCRIPTION WHERE EMAIL = '{email}' AND ROWNUM < 2")
    #     res = self.cursor.fetchall()
    #     for row in res:
    #         print(row[0])

    

    