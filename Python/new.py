# def my_func(name):
#     print("hii {}".format(name))
#
# my_func("Prajwal")
#
#
# def My_functn():
#     name = "praju"
#     age = 21
#     place= "Mandya"
#     print ("Hello My name is {} my age is {} and i am from {}".format(name,age,place))
# My_functn()
#

#Random
'''import  random
print(random.randint(1,10))
lis=[12,432,12,'pp',"pdaaa"]
print(random.choice(lis))'''

class student:
    def __init__(self,age):
        fname="PrajwalKumar"
        lname="B"
        self.age=age
        print(fname,lname,age)
    def format(self,fname,lname):
        return f'{fname},{lname},of age {self.age}'
class clg(student):
    def __init__(self,fname,lname,age):
        super().__init__(age)
        print(f"name if {fname} {lname} and age is {age}")



student1=student(22)
print(student1.format("Pranav","Shetty"))
student2=clg("Prajwal","Kumar",43)
print(student2)


