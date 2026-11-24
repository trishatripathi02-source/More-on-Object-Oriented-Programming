class I0String():

    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter String : ")

    def print_string(self):
        print("Result is : ", self.str1.upper())        

str1 = I0String()

str1.get_string()
str1.print_string