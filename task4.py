class Employee:
    def work(self):
        print("Employee is working.")        

class Manager(Employee): 
    def work(self):
        print("Manager is managing the team")

manager = Manager()
manager.work()        

class Developer(Employee):
    def work(self):
        print("Developer is writing code")
developer = Developer()
developer.work()
                     