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
            students_added=student_marks
        print("Here are added students marks:", students_added)
    elif ans=="2":
        name_todelete= input("Enter name of student to delete:")
        del students_added[name_todelete]
        print("\n Student Deleted")
    elif ans=="3":
        query_name = input("Enter name of student:")
        avg_dic={}
        for k,v in student_marks.items():
            avg_dic[k]=mean(v)
        print('Student marks:', student_marks[query_name])
        print("Student average marks: %.2f" %avg_dic[query_name])
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
