# ------------------------------------------------------------------------------------------ #
# Title: Assignment_06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Ericka Moreno, 11/20/24, Assignment_06_Functions
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the variables
students: list = []  # a table of student data
menu_choice: str  = '' # Hold the choice made by the user.

# Define classes
class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ Reads data from json
        Ericka Moreno, 11/20/24, created function
        :return: List
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    def write_data_to_file(file_name: str, student_data: list):
        """ Writes data to json
        Ericka Moreno, 11/20/24, created function
        :return: none
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            IO.output_error_messages(message="Error with writing to the file", error=e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ Outputs error message
        Ericka Moreno, 11/20/24, created function
        """
        print(message, end= "\n\n")
        if error is not None:
            print("--Technical Error Message--")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    # Display menu of choices
    def output_menu(menu: str):
        """ Output options menu to choose from
        Ericka Moreno, 11/20/24, created function
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ Takes input from user for menu choice
        Ericka Moreno, 11/20/24, created function
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ Output student first name, last name and course
        Ericka Moreno, 11/20/24, created function
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ Takes data for student first name, last name and course
        Ericka Moreno, 11/20/24, created function
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="error in datatype", error=e)
        except Exception as e:
            IO.output_error_messages(message="There was an error with the data", error=e)
        return student_data

# Start of main code

# Define variable
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
