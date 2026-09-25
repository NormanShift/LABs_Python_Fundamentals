# LAB 9

# Part A - Polymorphism

# A:1 - A:5

class EmailNotification:
    def send(self):
        return "Sent E-mail to recipient"


class SMSNotification:
    def send(self):
        return "Notification sent to customer by SMS"


class PushNotification:
    def send(self):
        return "Pushed notification to mobile device"


# email = EmailNotification()
# sms = SMSNotification()
# push = PushNotification()

# m_srv = [
#     email.send(),
#     sms.send(),
#     push.send()
# ]

# print(m_srv)

msg_srv = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for message in msg_srv:
    print(message.send())

# print(email.send())
# print(sms.send())
# print(push.send())

# Explanation: In this example, each object has a method called send(). There is no inheritance taking place, so talking about each object having it's own implementation of an inherited member does not apply here. But it's still polymorphism.

#-------------------------------------


# Part B - Polymorphism with inheritance

# B:1 to B:5

class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "This is the main Document."


class PDFDocument(Document):
    # __init__ runs on the inherited baseclass
    def describe(title):
        return "The PDF is a Document."


class TextDocument(Document):
        # __init__ runs on the inherited baseclass
        def describe(title):
            return "Text is also a Document."


subdocs = [
    PDFDocument("Booklets"),
    TextDocument("Let there be Books"),
    PDFDocument("The Drafted Man"),
    TextDocument("Entitled and Title-mente")
]


titles = subdocs[1]

for doc in subdocs:
    print(f"{doc.title}: {doc.describe()}")



#-------------------------------------

# Part C - Duck typing

# C:1 - C:5

class Printer:
    def output(self):
        return "The Printer prints."

class Screen:
    def output(self):
        return "The Screen emits."

peripherals = [
    Printer(),
    Screen()
]

for out in peripherals:
    print(out.output()) # Uses "Duck Typing"

# Explanation: Robot and Dog do not inherit from the same base class, but both
# provide the same method. This works because of duck typing:
# if an object has the required method, Python can use it without
# requiring a shared parent class.


#-------------------------------------


# Part D - isinstance()

# D:1 - D:5

class User:
    def __init__(self):
        pass

class AdminUser(User):
    pass


admin = AdminUser()

is_admin_admin = isinstance(admin, (AdminUser))
is_admin_user = isinstance(admin, (User))
is_admin_string = isinstance(admin, (str))

print("Is AdminUser an AdminUser:", is_admin_admin)
print("Is AdminUser also a User:", is_admin_user)
print("Is AdminUser a String:", is_admin_string)

# Explanation: The instance of AdminUser is also considered to be a User because AdminUser inherits the members of the User class.

#-------------------------------------

# Part E - __str__

# E:1 - E:5

# Without __str__ the output is: <__main__.Product object at 0x00000174BE0F7A10>

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
        

# product = Product("Karl Ada", 105)

# print(product)


# Using __str__ "magic method" below:

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price} Skr"
        

product = Product("Cliché Generator", 1059.95)
produgjd = Product("Hair Dryer Deluxe Ed.", 5555.55)
produc = Product("Powder Toast Man Figurine", 499.50)
project = Product("Traumatizer", 9999.99)


print(product)
print(produgjd)
print(produc)
print(project)

prod_str = str(product)

print("Object Type:", type(prod_str))


#-------------------------------------

# Part F - __str__ with inheritance

# F:1 - F:5

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Name: {self.owner}\nPrice: ${self.balance}"


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Name: {self.owner}\nPrice: {self.balance}\niRate: {self.interest_rate}"


account = Account("Girbraldazaar Gülasch", 200000)

savings_acc = SavingsAccount("Margot Touchér", 500000, 0.02)

print(account)
print(savings_acc)

#-------------------------------------
# Part G - Inheritance or composition?

class CPU:
    def __init__(self, model):
        self.model = model

# This uses composition rather than inheritance.
class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu

# Create a CPU object and pass it to a Computer object.
cpu1 = CPU("AMD Ryzen")
computer1 = Computer("ASUS", cpu1)

# Print the computer brand and CPU model through the Computer object.
print("Computer brand:", computer1.brand)
print("CPU model:", computer1.cpu.model)

# Computer HAS-A CPU makes more sense than Computer IS-A CPU.
# A CPU is one component contained inside a computer.
# A computer is not a specialized type of CPU, so inheritance
# would not describe the relationship correctly.

# G:6
# Decide between inheritance and composition for each pair.

# Car / Engine:
# Composition because a Car HAS-A Engine.
# A Car is not a type of Engine.

# Manager / Employee:
# Inheritance because a Manager IS-AN Employee.
# Manager can inherit common Employee attributes and methods.

# Course / Teacher:
# Composition because a Course HAS-A Teacher.
# A Course is not a type of Teacher.

# Phone / Device:
# Inheritance because a Phone IS-A Device.
# Phone can inherit common Device attributes and methods.

#-------------------------------------


# Part H - Applied challenge: Export system

# H:1

class Exporter:
    def export(self, data):
        self.data = data
        return "This is the baseclass."
    def __str__(self):
        return "Generic Exporter"

class ConsoleExporter(Exporter):
    def export(self, data):
        self.data = data
        return f"ConsoleExporter Data: {self.data}"
    def __str__(self):
        return "Console Exporter. Overrides export() ."

class TextExporter(Exporter):
    def export(self, data):
        self.data = data
        return f"TextExporter Data: {self.data}"
    def __str__(self):
        return "Text Exporter. Overrides export() ."


class SummaryExporter(Exporter):
    def export(self, data):
        self.data = data
        return f"Summary Exporter Data: {self.data}"
    def __str__(self):
        return f"Summary Exporter. DataOverrides export() ."


class AddedExporterClass:
    def export(self, data):
        self.data = data
        return f"Added Exporter Data: {self.data}"
    def __str__(self):
        return f"No inheritance. Added Exporter. DataOverrides export() ."

# Defining a list for demonstrating polymorphism when iterated on (if).
exporters = [
    ConsoleExporter(),
    TextExporter(),
    SummaryExporter(),
    AddedExporterClass()
]

number = 1567

for value in exporters:
    print(value.export(number))

# print(Exporter().export(120))
# print(ConsoleExporter().export(1500))
# print(ConsoleExporter())
# print(TextExporter().export(12578))
# print(SummaryExporter().export(322))






#-------------------------------------
