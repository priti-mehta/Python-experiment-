#student marks ,percentage and grade 
name = input ("Enter student name :")
n = int (input ("Enter number of subjects:"))
total = 0
for i in range (1,n+1):
    mark = float  (input (f"Enter mark for subject {i}:"))
    total += mark 
    percentage = total / n
    if percentage >= 90:
        grade = "A+"
        performance = "outstanding"
    elif percentage >=80:
        grade ="A"
        performance = "Excellent"
    elif percentage >=70:
        grade = "B"
        performance = "very good"
    elif percentage >=60:
        grade = "C"
        performance = "good"
    elif  percentage >= 50:
        grade ="D" 
        performance = "Average"
    else:
        grade = "F"
        performance = "Needs Improvement"
        print ("\n---academic performance ---")
        print ("student name :",name)
        print ("total marks :",total)
        print ("percentage :",round (percentage ,2),"%")
        print ("grade:",grade)
        print ("performance :",performance )
