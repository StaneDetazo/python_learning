class Customer :
    def setName(self, new_name, age) :
        self.name = new_name
        self.age = age

customer1 = Customer()
customer1.setName("test", 12)
print(customer1.name)
print(customer1.age)