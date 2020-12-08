from sqlite3 import *

#
# def creating_table():
#     conn = connect("add_new_student.db")
#     cur = conn.cursor()
#     query = """CREATE TABLE add_student (roll_number INT PRIMARY KEY, fall TEXT, std_name TEXT, std_last_name TEXT,
#      std_father_name TEXT, cnic_no INT, std_age INT, father_phone_number INT)"""
#     cur.execute(query)
#     conn.commit()
#     conn.close()
#
# # creating_table()
#
#
# def add_data_into_table(roll_number, fall, std_name, std_last_name, std_father_name, cnic_no, std_age, father_phone_no):
#     conn = connect("add_new_student.db")
#     cur = conn.cursor()
#     query = """INSERT INTO add_student (roll_number, fall, std_name, std_last_name, std_father_name, cnic_no,
#      std_age, father_phone_number)
#      VALUES(""" + str(roll_number) + ",'" + str(fall) + "','" + str(std_name) + "','" + str(std_last_name) + "','" + \
#             str(std_father_name) + "'," + str(cnic_no) + "," + str(std_age) + "," + str(father_phone_no) + ")"
#     cur.execute(query)
#     conn.commit()
#     conn.close()
#
#
# # add_data_into_table(2, 'f19', 'Husnain', 'Ali', 'Amin', 12534122544, 40, 30163213)
#
#
# def read_data():
#     conn = connect("add_new_student.db")
#     cur = conn.cursor()
#     query = """SELECT * FROM  add_student"""
#     cur.execute(query)
#     take_data = cur.fetchall()
#
#     # take_data = cur.fetchall()
#     conn.commit()
#     conn.close()
#     # print(take_data)
#     return take_data
#
#
# def createString():
#     allReceivedRecords = read_data()
#     # print(allReceivedRecords)
#     allRecordsString = "Roll Number\t\tFall\t\tStudent Name\t\tLast Name\t\tFather Name\t\tCNIC Number\t\tStudent Age\t\tStudent Father Number \n"
#     allRecordsString = allRecordsString + "============================================================================================================================"
#     for eachRecord in allReceivedRecords:
#         allRecordsString = allRecordsString + "\n"
#         for eachValue in eachRecord:
#             allRecordsString = allRecordsString + str(eachValue) + "\t\t"
#     # print(allRecordsString)
#     return allRecordsString
#
#
#
# ###################################### READ STUDENT CODE #########################################
#
#
# class read_student_data():
#
#     def __init__(self):
#         # read_file_time_start = time.time()
#         read_student_window = Tk()
#         read_student_window.title("View Student Recode")
#         read_student_window.configure(bg="#425942")
#         read_student_window.state("zoomed")
#
#         making_label = Label(read_student_window, text="View Student Recode", font=("Algerian", 20, "bold"), fg="White", bg="#425942")
#         making_label.pack()
#
#         # making Frame Right Down
#
#         Frame_right_down = Frame(read_student_window, bg="#425942")
#         Frame_right_down.pack(side=BOTTOM, fill=X)
#
#         # makng show Button
#
#         button_show = Button(Frame_right_down, text="Show", font=("Bold", 15), command=lambda: [read_student_window_text_box.insert('1.0', createString())])
#         button_show.pack(side=LEFT, pady=10, padx=30)
#         # Making Text Box
#
#         read_student_window_text_box = Text(read_student_window, height=41, width=170)
#         read_student_window_text_box.pack()
#
#         # making Quit Function
#
#         def destroy():
#             read_student_window.destroy()
#
#         # making Quit Button
#
#         quit_button = Button(Frame_right_down, text='Quit', font=("Bold", 15), command=lambda: destroy())
#         quit_button.pack(side=RIGHT, pady=10, padx=30)
#
#         # making Time Label
#
#         label_time = Label(Frame_right_down, text="Require Time: ", fg="White", bg="#425942")
#         label_time.pack(side=LEFT, pady=10, padx=30)
#
#         # making Time text
#
#         time_recode_text = Text(Frame_right_down, width=20, height=1)
#         time_recode_text.pack(side=LEFT, pady=10, padx=30)
#
#         # making size label
#
#         size_label = Label(Frame_right_down, text="File Size In Bytes", fg="White", bg="#425942")
#         size_label.pack(side=LEFT, pady=10, padx=30)
#
#         # making size text
#
#         size_text = Text(Frame_right_down, width=20, height=1)
#         size_text.pack(side=LEFT, pady=10, padx=30)
#
#         read_student_window.mainloop()


def read_file_function():
    r1 = read_student_data()