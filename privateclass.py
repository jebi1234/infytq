class Customer:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def view_details(self):
        print(self.name,self.age)
        print(self.address.get_door(),self.address.get_city())
class Address:

    def __init__(self,door,city):
        self.__door=door
        self.__city=city
        def get_door(self):
            return self.__door
        def get_city(self):
            return self.__city
add1=Address(123,"nandyal")
cust1=Customer("jabi",20,add1)
cust1.view_details()