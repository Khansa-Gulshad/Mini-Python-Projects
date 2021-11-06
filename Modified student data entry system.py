import pandas as pd
ans=True
while ans:
    print("Welcome to student data system")
    print("""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
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
        print("Here are added students marks:\n", df)
    elif ans=="2":
        name_todelete= input("Enter name of student to delete data:") # enter name of student to delete
        df = df.drop(df[df['Student Name']==name_todelete].index) # delete student data here
        print("\n Student Deleted")
        print(df) #dataframe after deleting student data
    elif ans=="3":
        query_name = input("Enter name of student:")
#         # find student rank among others, percentage
        df['Total marks'] = df.sum(axis=1) # total marks for each student
        df['Percentage'] = (df['Total marks']/400)*100 # percentage for each student
        df['Rank'] = df['Percentage'].rank(method='dense', ascending=False) # rank for each student based on percentage
        print(df)
        print('Student total marks out of 400:\n', df.loc[df['Student Name'] == query_name]['Total marks'].values)
        print("Student percentage:\n",df.loc[df['Student Name'] == query_name]['Percentage'].values)
        print("Student rank is:\n",df.loc[df['Student Name'] == query_name]['Rank'].values)
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
