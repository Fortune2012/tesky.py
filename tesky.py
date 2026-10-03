students = {'Mercy': 200 , 'Nana kofi': 275,'fortune': 301, 'Kwame': 288, 'Ama': 265}

name = input("Enter the name of the student: ")

scores = []

for student, score in students.items():
    if student == name:
        print(f"{student}: {score / 5 }%")

        print(f"{max(students)} is the highest scorer.")
        print(f'{min(students)} is the lowest scorer.')
