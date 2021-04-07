import databaseConnection as dc

cur = dc.mydb.cursor()


class Airplane:
   def insert(self):
      reg_no = input("Enter registration number: ")
      model_no = input("Enter Model number: ")
      val = (reg_no, model_no)
      insert_query = """INSERT INTO Airplane VALUES(%s, %s)"""
      cur.execute(insert_query, val)
      dc.mydb.commit()
      o = Airplane()
      o.display()

   def delete(self):
      reg_no = input("Enter registration number: ")
      delete_query = """DELETE FROM Airplane WHERE reg_no = %s"""
      cur.execute(delete_query, (reg_no,))

   def display(self):
      cur.execute("SELECT *FROM Airplane")
      Rows = cur.fetchall()
      for Row in Rows:
         print(Row)


class Model:
   def insert(self):
      model_no = input("Enter Model number: ")
      capacity = input("Enter capacity : ")
      weight = input("Enter Weight : ")
      val = (model_no, capacity, weight)
      insert_query = """INSERT INTO Model VALUES(%s, %s, %s)"""
      cur.execute(insert_query, val)
      dc.mydb.commit()
      o = Model()
      o.display()

   def delete(self):
      model_no = input("Enter Model number: ")
      delete_query = """DELETE FROM Model WHERE model_no = %s"""
      cur.execute(delete_query, (model_no,))

   def display(self):
      cur.execute("SELECT *FROM Model")
      Rows = cur.fetchall()
      for Row in Rows:
         print(Row)


class Employee:
   def insert(self):
      mem_no = input("Enter Membership number: ")
      salary = input("Enter salary : ")
      phone_no = input("Enter Phone no : ")
      city = input("Enter city : ")
      f_name = input("Enter first name : ")
      l_name = input("Enter last name : ")
      faa_no = input("Enter FAA number : ")
      val = (mem_no, salary, phone_no, city, f_name, l_name, faa_no)
      insert_query = """INSERT INTO Employee VALUES(%s, %s, %s, %s, %s, %s, %s)"""
      cur.execute(insert_query, val)
      dc.mydb.commit()
      o = Employee()
      o.display()

   def delete(self):
      mem_no = input("Enter Membership number: ")
      delete_query = """DELETE FROM Employee WHERE Membership_no = %s"""
      cur.execute(delete_query, (mem_no,))

   def display(self):
      cur.execute("SELECT *FROM Employee")
      Rows = cur.fetchall()
      for Row in Rows:
         print(Row)


class Technician:
   def insert(self):
      mem_no = input("Enter Membership number: ")
      faa_no = input("Enter faa number : ")
      val = (mem_no, faa_no)
      insert_query = """INSERT INTO Technician VALUES(%s, %s)"""
      cur.execute(insert_query, val)
      dc.mydb.commit()
      o = Technician()
      o.display()

   def delete(self):
      mem_no = input("Enter membership number: ")
      delete_query = """DELETE FROM Technician WHERE Membership_no = %s"""
      cur.execute(delete_query, (mem_no,))

   def display(self):
      cur.execute("SELECT *FROM Technician")
      Rows = cur.fetchall()
      for Row in Rows:
         print(Row)


class TrafficController:
   def insert(self):
      date_of_exam = input("Enter Date of exam: ")
      faa_no = input("Enter faa number : ")
      reg_no = input("Enter registration number of airplane : ")
      mem_no = input("Enter membership number: ")
      val = (date_of_exam, faa_no, reg_no, mem_no)
      insert_query = """INSERT INTO Traffic_Controller VALUES(%s, %s, %s, %s)"""
      cur.execute(insert_query, val)
      dc.mydb.commit()
      o = TrafficController()
      o.display()

   def delete(self):
      mem_no = input("Enter membership number: ")
      delete_query = """DELETE FROM Traffic_Controller WHERE mem_no = %s"""
      cur.execute(delete_query, (mem_no,))

   def display(self):
      cur.execute("SELECT *FROM Traffic_Controller")
      Rows = cur.fetchall()
      for Row in Rows:
         print(Row)

class Test:
   def insert(self):
      Test_Date= input("Enter Date of exam: ")
      Test_Name = input("Enter name of exam : ")
      Test_Score = input("Enter Score : ")

      val = (Test_Date, Test_Name, Test_Score)
      insert_query2 = """INSERT INTO Test(Test_Date, Test_Name, Test_Score) VALUES(%s, %s, %s)"""
      print(val)
      cur.execute(insert_query2, val)
      dc.mydb.commit()
      o = Test()
      o.display()

   def delete(self):
      faa_no = input("Enter faa number: ")
      delete_query = """DELETE FROM Test WHERE FAA_number = %s"""
      cur.execute(delete_query, (faa_no,))

   def display(self):
      cur.execute("SELECT *FROM Test")
      Rows = cur.fetchall()
      for Row in Rows:
         print(Row)


class AirplaneSystem:
   def allTablesNames(self):
      print("Tables present in Database : ")
      print("1. Airplane\n2. Model\n3. Employee\n4. Technician\n5. Traffic Controller\n6. Test")
      print("Enter number of table to perform operations : ")
      choice = int(input())
      if choice == 1:
         obj = Airplane()
         print("Enter 1.To Insert record\n\t  2.To delete record\n\t  3.To display Table ")
         ch = int(input())
         if ch == 1:
            obj.insert()
         elif ch == 2:
            obj.delete()
         elif ch == 3:
            obj.display()
      elif choice == 2:
         obj = Model()
         print("Enter 1.To Insert record\n\t  2.To delete record\n\t  3.To display Table ")
         ch = int(input())
         if ch == 1:
            obj.insert()
         elif ch == 2:
            obj.delete()
         elif ch == 3:
            obj.display()
      elif choice == 3:
         obj = Employee()
         print("Enter 1.To Insert record\n\t  2.To delete record\n\t  3.To display Table ")
         ch = int(input())
         if ch == 1:
            obj.insert()
         elif ch == 2:
            obj.delete()
         elif ch == 3:
            obj.display()
      elif choice == 4:
         obj = Technician()
         print("Enter 1.To Insert record\n\t  2.To delete record\n\t  3.To display Table ")
         ch = int(input())
         if ch == 1:
            obj.insert()
         elif ch == 2:
            obj.delete()
         elif ch == 3:
            obj.display()
      elif choice == 5:
         obj = TrafficController()
         print("Enter 1.To Insert record\n\t  2.To delete record\n\t  3.To display Table ")
         ch = int(input())
         if ch == 1:
            obj.insert()
         elif ch == 2:
            obj.delete()
         elif ch == 3:
            obj.display()
      elif choice == 6:
         obj = Test()
         print("Enter 1.To Insert record\n\t  2.To delete record\n\t  3.To display Table ")
         ch = int(input())
         if ch == 1:
            obj.insert()
         elif ch == 2:
            obj.delete()
         elif ch == 3:
            obj.display()
      else:
         print("Enter valid number.")


AS = AirplaneSystem()
AS.allTablesNames()
dc.mydb.commit()




