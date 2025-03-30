from time import strftime
# For csv file creation
def create_file(file_name):
    """Creates a new attendance file with headers."""
    header = "Date,Topic"
    n = int(input("Enter number of students in your class :"))
    for i in range(1, n+1):
        name = input(f"Enter name of student [{i}] : ").title()
        header += "," + name
    else:
        header += "\n"
        with open(file_name, 'w') as f:
            f.write(header)
    print(f"File '{file_name}' created successfully!")

def read_file(file_name):
    with open(file_name, "r") as f:
        header = f.readline()
    return header[:-1:].split(",")[2:]

# For Daily Attendance
def attendance(file_name):
    ''' This is a daily purpose automation for the 'Teachers Specially'
        for the Attendance of their Students.
        Only enter (CSV) file name for daily attendance.
        Note : In this CSV file first column must be a "Date" column 
                and Second column "Topic" and in other columns name
                of the all students.
        '''
    temp = read_file(file_name)
    topic = input("Enter Topic name : ").title()
    header = strftime("%D") + "," + topic
    for j in temp:
        attendance = input(f"Enter Present(P) or Absent(A) for {j} : ").upper()[0]
        header += "," + attendance
    else:
        header += "\n"
    with open(file_name, 'a') as f1:
        f1.write(header)
    print("Attendance recorded successfully!")

# Main execution
if __name__ == "__main__":
    choice = input("Do you want to create a new file? (yes/no): ").strip().lower()
    if choice == 'yes':
        file_name = input("Enter Attendance File name: ") + ".csv"
        create_file(file_name)
    else:
        file_name = input("Enter existing CSV file name: ") + ".csv"
        attendance(file_name)
