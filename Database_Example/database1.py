import sqlite3
print("\n\n")

database1 = sqlite3.connect("C:/Users/0haigb36.UNI/Downloads/mysports.db")
db1cursor = database1.cursor()
db1cursor.execute("SELECT * FROM product")
print(db1cursor.fetchone())

print("\n\n")

db1cursor.execute("""SELECT custid, area, name 
                  FROM customer""")
for row in db1cursor.fetchall():
      print(row)

print("\n\n")

db1cursor.execute("""SELECT custid, area, name 
                  FROM customer""")
for row in db1cursor.fetchall():
      print(row[0],row[1],"   ",row[2])

print("\n\n")

customer_id = input("Enter Customer ID\n")

db1cursor.execute("""SELECT * FROM customers)

if customer_id not in 

db1cursor.execute("""SELECT custid, area, name 
                  FROM customer
                  WHERE UPPER(custid)=UPPER(?) """,(customer_id,))
for row in db1cursor.fetchall():
      print(row[0],row[1],"   ",row[2])