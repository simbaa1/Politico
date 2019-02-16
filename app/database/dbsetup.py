import psycopg2 as ps
import os
import psycopg2
from instance.config import app_config
from psycopg2.extras import RealDictCursor
from .schema import tables
from werkzeug.security import generate_password_hash


class DatabaseConnection:
    def __init__(self, config_name):
        self.config_name = config_name
        
    def connection(self):
        config = app_config[self.config_name].db_url
        print(config)

        try:
            global con, cur
            con = psycopg2.connect(config)
            cur = con.cursor(cursor_factory=RealDictCursor)
            print("Connection successful")
            
        except Exception as e:
            print(e)
   
    def create_all_tables(self):
        try:
            for q in tables:
                cur.execute(q)
            con.commit()
            print("Tables have beenc created successfully")
            con.close()

        except Exception as e:
            print(e)

    def create_admin_user(self):
        query = """ SELECT * FROM user WHERE email = 'simbakriss@gmail.com'
              """
        cur.execute(query)
        

        # if not user:
        #     cur.execute("INSERT INTO user(firstname, lastname, othername, email, \ phonenumber, passportUrl, password, isAdmin) VALUES('Chris', 'Simba', 'Omurwa', 'simbakriss@gmail.com', \ '0750502334', 'kingdwe.png', '{}', True)").format(generate_password_hash('12simbaa')))
        #     con.commit()



