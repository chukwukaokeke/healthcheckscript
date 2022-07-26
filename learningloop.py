#admin and user 

class Employee:
    def __init__(self,username,accesslevel):
        self.username=username
        self.accesslevel = accesslevel
        

    def makeadmin(self):
        self.accesslevel="admin"

    def readfile(self):
        if self.accesslevel == "admin" :
            print ("success")
        else:
            print ("no success")



p1 = Employee("tim123","admin")  
p2 = Employee("james234","user")

p1.readfile()

#p2.makeadmin()

p2.readfile()