import psycopg2
from faker import Faker

con = psycopg2.connect(database="customers", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")
print("Database opened successfully")
cur = con.cursor()
cur.execute('''CREATE TABLE CUSTOMER
       (ID INT PRIMARY KEY     NOT NULL,
       Name           TEXT    NOT NULL,
       Age INT NOT NULL,
       Address            TEXT     NOT NULL,
       review        TEXT);''')
print("Table created successfully")
fake = Faker()
for i in range(100000):
    print(i)
    cur.execute("INSERT INTO CUSTOMER (ID,Name,Age, Address,review) VALUES ('"+ str(i)+"','"+fake.name()+"','"+str(fake.random_int(min=5, max=70))+"','"+fake.address()+"','"+fake.text()+"')")
    con.commit()
