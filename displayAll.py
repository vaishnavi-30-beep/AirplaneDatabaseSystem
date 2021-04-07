
import databaseConnection as dc
cur2 = dc.mydb.cursor()

print("Airplane Table :")
cur2.execute("SELECT *FROM Airplane")
rows = cur2.fetchall()
for row in rows:
  print(row)
print("Model Table :")
cur2.execute("SELECT *FROM Model")
rows = cur2.fetchall()
for row in rows:
  print(row)
print("Employee Table :")
cur2.execute("SELECT *FROM Employee")
rows = cur2.fetchall()
for row in rows:
   print(row)
print("Technician Table :")
cur2.execute("SELECT *FROM Technician")
rows = cur2.fetchall()
for row in rows:
  print(row)
print("Traffic_Controller Table :")
cur2.execute("SELECT *FROM Traffic_Controller")
rows = cur2.fetchall()
for row in rows:
  print(row)
print("Test Table :")
cur2.execute("SELECT *FROM Test")
rows = cur2.fetchall()
for row in rows:
  print(row)
