from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees =Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name =input("Enter the name of the employee: ")
    if employee :=Employee.find_by_name(name):
        try:
            print(employee)
        except Exception as exc:
            print("Error finding employee: ", exc)
    else:
        print(f'Employee {name} not found')


def find_employee_by_id():
    id=input("Enter employee's id: ")
    if employee :=Employee.find_by_id(id):
        try:
            print(employee)
        except Exception as exc:
            print("Error finding employee: ", exc)
    else:
        print(f'Employee {id} not found')

def create_employee():
    name =input('Employee Name: ')
    job_title =input('Job Title: ')
    department_id =input('Department ID:')
    department_id = int(department_id)
    if Department.find_by_id(department_id):
        try:
            employee = Employee.create(name, job_title, department_id)
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error creating employee: ", exc)
    else:
        print(f'Department {department_id} not found')



def update_employee():
    employee_id =input("Enter employee ID: ")
    if employee :=Employee.find_by_id(employee_id):
        try:
            name =input('Employee Name: ')
            job_title =input('Job Title: ')
            department_id =input('Department ID:')
            department_id = int(department_id)
            if Department.find_by_id(department_id):
                employee.name = name
                employee.job_title = job_title
                employee.department_id = department_id
                employee.update()
                print(f'Success: {employee}')
            else:
                print(f'Department {department_id} not found')
        except Exception as exc:
            print("Error updating employee: ", exc)


def delete_employee():
    employee_id =input("Enter employee ID: ")
    if employee :=Employee.find_by_id(employee_id):
        employee.delete()
        print(f'Employee {employee_id} deleted')
    else:
        print(f'Employee {employee_id} not found')


def list_department_employees():
    department_id =input("Enter department ID: ")
    if department :=Department.find_by_id(department_id):
        try:
            for employee in department.employees():
                print(employee)
        except Exception as exc:
            print("Error finding department: ", exc)
    else:
        print(f'Department {department_id} not found')