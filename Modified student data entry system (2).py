import pandas as pd
ans=True
while ans:
    print("Welcome to student data system")
    print("""
    1.Create students dataframe
    2.Check Students data stored in system
    3.Add Students data to already exisiting dataframe
    4.Edit Students data
    5.Delete a Student
    6.Look Up Student Record
    7.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
        n = int(input("How many students? "))
        student_marks = {} 
        for _ in range(n):
            name, *line = input("Enter students name and score").split() # enter name with marks-space in between and one by one
            scores = list(map(float, line))
            student_marks[name] = scores
            df = pd.DataFrame.from_dict(student_marks, orient="index").reset_index()
            df.columns=['Student Name', 'English', 'Maths', 'Chemistry', 'Physics']
            students_data=df.to_csv('students_data.csv', index=False)
        print("Here are added students marks:\n", df)   
    elif ans=="2":
        print("\n Data of students stored in system:")
        students_data=pd.read_csv('students_data.csv', index_col=False)
        print(students_data)
    elif ans=="3":
        n = int(input("How many students? "))
        for _ in range(n):
            data_toadd= input("Enter students name and score").split() 
            students_data.loc[len(students_data.index)] = data_toadd
            students_data=students_data.to_csv('students_data.csv', index=False)
            students_data=pd.read_csv('students_data.csv', index_col=False)
        print(students_data) 
    elif ans=="4":
        index_toedit= int(input("Enter Row Index to edit data:")) #student name index
        marks_toedit= input("Enter subject of student to edit marks data:")
        students_data.at[index_toedit,marks_toedit]=input("Enter new marks:")
        print("\n Student Data edited")
        print(students_data)
    elif ans=="5":
        name_todelete= input("Enter name of student to delete data:") # enter name of student to delete
        students_data = students_data.drop(students_data[students_data['Student Name']==name_todelete].index) # delete student data here
        print("\n Student Deleted")
        print(students_data) #dataframe after deleting student data
    elif ans=="6":
        query_name = input("Enter name of student:")
#         # find student rank among others, percentage
        students_data['Total marks'] = students_data.sum(axis=1)
        students_data['Percentage'] = (students_data['Total marks']/400)*100
        students_data['Rank'] = students_data['Percentage'].rank(method='dense', ascending=False)
        print(students_data)
        print('Student total marks out of 400:\n', students_data.loc[students_data['Student Name'] == query_name]['Total marks'].values)
        print("Student percentage:\n",students_data.loc[students_data['Student Name'] == query_name]['Percentage'].values)
        print("Student rank is:\n",students_data.loc[students_data['Student Name'] == query_name]['Rank'].values)
    elif ans=="7":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
