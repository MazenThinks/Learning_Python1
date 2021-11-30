class personal_id :
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def my_func(self):
        print("My name is " + self.name)

id = personal_id("Thorfinn" , "15")
id.my_func()