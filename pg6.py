from tkinter import *
import databaseConnection as dc

cur = dc.mydb.cursor()

root = Tk()
root.title("Test Table")
root.geometry("1000x900")
root.configure(bg='white')

frame = Frame(root)
frame.configure(bg='white')
frame.pack()

table_name = Label(frame, text="Test Table", fg='brown', bg='white', padx=5, pady=5)
table_name.pack()
table_name.configure(font=("Helvetica", 16, "bold"))

FAA_label = Label(frame, text="Enter FAA number: ", bg='white', fg="red", padx=5, pady=5)
FAA_label.pack()

entry1 = Text(frame, height=1, width=20, padx=5, pady=5)
entry1.pack()
entry1.configure(font=("Helvetica", 16))


test_date_label = Label(frame, text="Enter test date : ", bg='white', fg="red", padx=5, pady=5)
test_date_label.pack()

entry2 = Text(frame, height=1, width=20, padx=5, pady=5)
entry2.pack()
entry2.configure(font=("Helvetica", 16))

test_name_label = Label(frame, text="Enter test name : ", bg='white', fg="red", padx=5, pady=5)
test_name_label.pack()

entry3 = Text(frame, height=1, width=20, padx=5, pady=5)
entry3.pack()
entry3.configure(font=("Helvetica", 16))

test_score_label = Label(frame, text="Enter test score : ", bg='white', fg="red", padx=5, pady=5)
test_score_label.pack()

entry4 = Text(frame, height=1, width=20, padx=5, pady=5)
entry4.pack()
entry4.configure(font=("Helvetica", 16))


class Test:

    def clear(self):
        entry1.delete('1.0', END)
        entry2.delete('1.0', END)
        entry3.delete('1.0',END)
        entry4.delete('1.0',END)

    def insert(self):
        insert_query = """INSERT INTO model(model_no,capacity,weight) VALUES(%s, %s, %s)"""
        faa_no = entry1.get(1.0, 'end-1c')
        test_date = entry2.get(1.0,'end-1c')
        test_name = entry3.get(1.0,'end-1c')
        test_score = entry4.get(1.0,'end-1c')
        val = (faa_no,test_date,test_name,test_score)
        if faa_no != "" and test_date != "" and test_name != "" and test_score != "":
            cur.execute(insert_query, val)
            dc.mydb.commit()

    def delete(self):
        delete_query = """DELETE FROM test WHERE FAA_number = %s"""
        faa_no = entry1.get(1.0, 'end-1c')
        cur.execute(delete_query, (faa_no))
        dc.mydb.commit()

    def display(self):
        cur.execute("SELECT *FROM Test")
        Rows = cur.fetchall()
        for Row in Rows:
            print_label = Label(frame, text=Row, bg='white', fg="blue", padx=5, pady=5)
            print_label.pack()
            print_label.configure(font=("Helvetica", 16))
            print(Row)

    def update(self):
        faa_no = entry1.get(1.0, 'end-1c')
        test_date = entry2.get(1.0,'end-1c')
        test_name = entry3.get(1.0,'end-1c')
        test_score = entry4.get(1.0,'end-1c')
        update_query = """update Test set Test_Date = %s, Test_Name = %s, Test_Score = %s where FAA_number = %s"""
        val = (test_date,test_name,test_score, faa_no)
        cur.execute(update_query,val)
        dc.mydb.commit()


    def back(self):
        root.destroy()
        import UI

obj = Test()
blank = Label(frame,bg='white', padx=15, pady=15)
blank.pack()
b1 = Button(frame, height=2, width=10, text='Insert', command=obj.insert, bg='black', fg='white',
            padx=5, pady=5)
b1.pack(side=LEFT)
b2 = Button(frame, text='Delete', height=2, width=10, command=obj.delete, bg='black', fg='white', padx=5, pady=5)
b2.pack(side=LEFT)
b3 = Button(frame, text='Display', height=2, width=10, command=obj.display, bg='black', fg='white', padx=5, pady=5)
b3.pack(side=LEFT)
b4 = Button(frame, text='Update', height=2, width=10, command=obj.update, bg='black', fg='white', padx=5, pady=5)
b4.pack(side=LEFT)
b5 = Button(frame, text='Clear', height=2, width=10, command=obj.clear, bg='black', fg='white', padx=5, pady=5)
b5.pack(side=LEFT)
back = Button(frame, text='Back', height=2, width=10, command=obj.back, bg='black', fg='white', padx=5, pady=5)
back.pack(side=LEFT)
blank = Label(frame, bg='white', padx=15, pady=15)
blank.pack()
root.mainloop()


'''
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
'''