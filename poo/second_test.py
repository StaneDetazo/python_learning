class Customer :
    def setName(self, new_name) :
        self.name = new_name

    def Identify(self) :
        print(f"i am customer {self.name}")

customer1 = Customer()
customer1.setName("test")
print(customer1.name)
customer1.Identify()