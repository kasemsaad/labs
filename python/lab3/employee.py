from  Human import Human

class employee(Human):
    def __init__(self,id,name,salary):
         super().__init__(name)
         self.id = id
         self.salary = salary

    def __str__(self):
     return f'Id = {self.id} Name = {self.name}  salary = {self.salary}'
