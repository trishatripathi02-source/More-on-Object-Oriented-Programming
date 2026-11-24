class Employee:

    def __init__(self):
        print("Employee Created")

    def __delf__(self):
        print("Destructor Called")

def Create_obj():
    print("Making Object....")
    obj = Employee()
    print("Function and....")
    return obj

print("Calling Create_obj() function....")
obj = Create_obj()
print("Program End....")