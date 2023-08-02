from datetime import date, datetime


user = []
student = {}

def registration(u_id, pwd):
    if not any(user['u_id'] == u_id for user in user):
        user.append({'u_id': u_id, 'pwd': pwd})
        print("You are successfully registered. log in to use services")
    else:
        print(f"The username '{u_id}' already exists, try with different username")

def login(u_id, pwd):
    if any(user['u_id'] == u_id and user['pwd'] == pwd for user in user):
        print(f"Hello {u_id}!")
        return True
    else:
        print("Entered details are invalid, Try again.")
        return False


def add_student(name, rollno, email, address):
    if rollno not in student:
        student[rollno] = {
            'Name': name,
            'Email': email,
            'Address': address
        }
        print(f"Student '{name}' information added successfully.")
    else:
        print(f"Student with Roll Number '{rollno}' already exists.")



def view_student(rollno):
    if rollno in student:
        student_info = student[rollno]
        print(f"Student Information for Roll Number '{rollno}':")
        for key, value in student_info.items():
            print(f"{key}: {value}")
    else:
        print(f"Student with Roll Number '{rollno}' not found in the database. Cannot view information.")



def update_Details(rollno, key, value):
    if rollno in student:
        student_info = student[rollno]
        if key in student_info:
            student_info[key] = value
            print(f"Student with Roll Number '{rollno}' information updated successfully.")
        else:
            print(f"Invalid key '{key}'. Cannot update.")
    else:
        print(f"Student with Roll Number '{rollno}' not found in the database.")

def deletedetails(rollno):
    if rollno in student:
        del student[rollno]
        print(f"Student with Roll Number '{rollno}' information deleted successfully.")
    else:
        print(f"Student with Roll Number '{rollno}' not found in the database. Cannot delete information.")


def validateinfo(rollno):
    if not rollno.isdigit():
        print("Invalid roll number. Roll number should contain digits only.")
        return False
    return True


def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        print("Invalid email address.")
        return False
    return True


def mark_attendance(rollno, date_str=None):
    today = date.today().strftime("%Y-%m-%d") if date_str is None else date_str
    if rollno in student:
        if 'Attendance' not in student[rollno]:
            student[rollno]['Attendance'] = {}
        attendance_data = student[rollno]['Attendance']

        if today in attendance_data:
            print(f"Attendance for Roll Number '{rollno}' on {today} has already been marked as '{attendance_data[today]}'.")
        else:
            while True:
                attendance = input(f"Mark attendance for Roll Number '{rollno}' on {today} (P for Present, A for Absent): ").upper()
                if attendance in ['P', 'A']:
                    attendance_data[today] = attendance
                    print(f"Attendance marked for Roll Number '{rollno}' on {today} as '{attendance}'.")
                    break
                else:
                    print("Invalid input. Please enter 'P' for Present or 'A' for Absent.")
    else:
        print(f"Student with Roll Number '{rollno}' not found in the database. Cannot mark attendance.")
                

def view_attendance_records(rollno):
    if rollno in student:
        attendance_dates = student[rollno]['Attendance']
        print(f"Attendance records for '{rollno}':")
        for date_str, attendance_status in attendance_dates.items():
            print(f"{date_str}: {attendance_status}")
    else:
        print(f"Student '{rollno}' not found in the database. Cannot view attendance records.")


def view_attendance_by_date(date_str):
    try:
        specific_date = datetime.strptime(date_str, "%Y-%m-%d")
        present_students = []

        for rollno, student_data in student.items():
            if 'Attendance' in student_data:
                attendance_dates = student_data['Attendance']
                if date_str in attendance_dates and attendance_dates[date_str] == 'P':
                    present_students.append(rollno)

        if present_students:
            print(f"Students present on {date_str}:")
            for value in present_students:
                print(f"Roll Number: {value}")
        else:
            print(f"No students were present on {date_str}.")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD' format.")


def main():

    logged_in = False
    should_continue = True

    while should_continue:
        print("\nWelcome to Attendance Management System. \
              Enter your choice!")
        if not logged_in:
            print("Press 'R' to Register")
            print("Press 'L' to Login")
            print("Press 'E' to Exit")
        else:
            print("a. Add Student")
            print("b. Remove Student")
            print("c. Mark Attendance")
            print("d. View Attendance")
            print("e. Manage Student Information")
            print("f. View Attendance Records Filter by Date")
            print("g. Logout")
            print("h. Exit")


        choice = input("Enter your choice: ")

        if not logged_in:
            if choice == "R":
                u_id = input("Enter a username : ")
                pwd = input("Enter Password: ")
                registration(u_id, pwd)

            elif choice == "L":
                u_id = input("Enter u_id: ")
                pwd = input("Enter pwd: ")
                logged_in = login(u_id, pwd)

            elif choice == "E":
                print("\nYou are now out of the system, thankyou for trying our system.")
                should_continue = False

            else:
                print("Invalid choice. Please try again.")

        else:
            if choice == 'a':
                 name = input("Enter student name: ")
                 while True:
                     rollno = input("Enter student roll number: ")
                     if validateinfo(rollno):
                         break;

                 while True:
                     email = input("Enter student email: ")
                     if validate_email(email):
                         break;
                 
                 
                 address = input("Enter address: ")
                 add_student(name, rollno, email, address)
                    

            elif choice == 'b':
                name = input("Enter student roll number: ")
                deletedetails(rollno)

            elif choice == 'c':
                rollno = input("Enter student roll number: ")
                date_str = input("Enter date (YYYY-MM-DD) to mark attendance (press Enter for today's date): ")
                if not date_str:
                    mark_attendance(rollno)
                else:
                    mark_attendance(rollno, date_str)
            

            elif choice == 'd':
                name = input("Enter student roll number: ")
                view_attendance_records(name)                

            elif choice == 'e':
                print("\nManage student Information")
                rollno = input("Enter student roll number: ")
                       
                print("1. View Student Information")
                print("2. Update Student Information")
                print("3. Delete Student Information")

                info_choice = int(input("Enter your choice: "))

                if info_choice == 1:
                    view_student(rollno)

                elif info_choice == 2:
                    key = input("Enter key (e.g., 'Address', 'Email'): ")
                    value = input("Enter new value: ")
                    if key == 'Email' and not validate_email(value):
                        continue
                    update_Details(rollno, key, value)
                    
                elif info_choice == 3:
                    deletedetails(rollno)

                else:
                    print("Invalid choice. Please try again.")

            elif choice == 'f':               
                date_str = input("Enter date (YYYY-MM-DD) to filter records: ")
                view_attendance_by_date(date_str)
                

            elif choice == 'g':
                logged_in = False
                print("\nLOGGED OUT")
                
            elif choice == 'h':
                print("\nYOU EXIT FROM THE SYSTEM")
                should_continue = False

            else:
                print("Invalid choice. Please try again.")
                                
                   
                
if __name__ == "__main__":
    main()           
                

        

         
        















































        

        
   
