
#number one
name= input("hello, what is your name? ")
print("hello " +name+".",''+"nice to meet you!")

#Number two'

celsius = float(input("enter a temperature in celsius: "))
Fahrenheit =  float((celsius * 9/5)) +32
print(celsius,"c",'' +"is equivalent to", (Fahrenheit),'' + "F")


#number three

NoStudents = int(input("enter the number of students: "))
group_size = int(input("Enter group size: "))
groups_needed = int(NoStudents/group_size)
leftovers =NoStudents - ( group_size* groups_needed) 
print("there will be ", +groups_needed,'groups with', +leftovers, "students left over.")

#number 4
Noofsweets = int(input("enter the number of sweets available: "))
pupil_attendance = int(input("Enter number of pupil in attendance: "))
amount_given = int(Noofsweets/pupil_attendance)
leftovers =Noofsweets - ( pupil_attendance* amount_given) 
print("Amount to give is ", +amount_given,'and you have', +leftovers, "leftovers")