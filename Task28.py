# Prepare the program which creates the initials from the Name and Surname entered
# by the user (eg. name: John, surname: Doe, initials: JD).

Name = input("Put your name: ")
Surname = input("Put your surname: ")

print(Name[0].upper(),Surname[0].upper(), sep ='.')

# alternatively
print(Name[0].upper()+'.'+Surname[0].upper())

