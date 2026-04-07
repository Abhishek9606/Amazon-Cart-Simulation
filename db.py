import sqlite3

conn = sqlite3.connect("products.db")
c  = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS customers(
cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
cust_name TEXT NOT NULL,
cust_mail_id  TEXT NOT NULL,
cust_password TEXT NOT NULL
)''')

c.execute('''CREATE TABLE IF NOT EXISTS products(
product_id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name TEXT NOT NULL,
product_description TEXT NOT NULL
)''')

c.execute("INSERT INTO products(product_name,product_description) VALUES('ToothPaste','Used to brush your teeth.')")
c.execute("INSERT INTO products(product_name,product_description) VALUES('Soap','Used to take bath.')")
c.execute("INSERT INTO products(product_name,product_description) VALUES('Ice cream','A favorite for children.')")
c.execute("INSERT INTO products(product_name,product_description) VALUES('BroomStick','Used to clean the rooom.')")


conn.commit()
conn.close()





