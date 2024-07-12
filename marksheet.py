nm = input("Enter Your Name :- ")
rn = int(input("Enter Your Roll No :- "))

cs = int(input("\nEntet the Mark 1 :- "))
py = int(input("Entet the Mark 2 :- "))
j2ee = int(input("Entet the Mark 3 :- "))
practical1 = int(input("Entet the Mark 4 :- "))
practical2 = int(input("Entet the Mark 5 :- "))

total=cs+py+j2ee+practical1+practical2
perc = total/5

print("\t\t----MarkSheet----\n")

print("Name :- ",nm)
print("Roll No. :- ",rn)

print("CyberSecurity :- ", cs)
print("Python:- ", py)
print("J2EE :- ", j2ee)
print("practical1 :- ", practical1)
print("practical2 :- ", practical2)

print("\nTotal Marks :- ",total)
print("Percentage :- ",perc)

if perc > 80:
    print("Pass With A Class")
elif (perc >= 60 and perc <80):
    print("Pass with B Class")
elif (perc >= 33 and perc <60):
    print("Pass")
else:
    print("Sorry You Are Fail...")
