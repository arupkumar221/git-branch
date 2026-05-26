# Simple Python Program

name = input("Enter your name: ")

print("Hello", name)
print("Welcome to Python Programming")

print=2000+3000+1000=6000




-------git branch commands------------


     git branch                  # show local branches
git branch -a               # show all branches
git checkout dev            # switch branch
git checkout -b dev         # create + switch branch
git switch dev              # switch branch (modern)
git switch -c feature       # create + switch branch
git merge dev               # merge dev into current branch
git branch -d dev           # delete branch
git branch -D dev           # force delete branch
git push origin dev         # push branch to remote
git pull origin main        # pull latest code
git fetch                   # fetch remote updates
git rebase main             # rebase current branch
git branch -m old new       # rename branch
git remote show origin      # check remote branches    
git push --set-upstream origin dev   # first push for new branch
  
     

        -----some code in pythonn-------------------


# Student Management System
# Medium Level Python Program

students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")

        students[roll] = {
            "name": name,
            "marks": marks
        }

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            print("\nStudent Records")
            for roll, data in students.items():
                print(f"Roll: {roll}")
                print(f"Name: {data['name']}")
                print(f"Marks: {data['marks']}")
                print("-------------------")

    elif choice == "3":
        search_roll = input("Enter Roll Number to Search: ")

        if search_roll in students:
            print("Student Found")
            print("Name:", students[search_roll]["name"])
            print("Marks:", students[search_roll]["marks"])
        else:
            print("Student not found")

    elif choice == "4":
        delete_roll = input("Enter Roll Number to Delete: ")

        if delete_roll in students:
            del students[delete_roll]
            print("Student deleted successfully")
        else:
            print("Student not found")

    elif choice == "5":
        print("Program Exited")
        break

    else:
        print("Invalid choice")
