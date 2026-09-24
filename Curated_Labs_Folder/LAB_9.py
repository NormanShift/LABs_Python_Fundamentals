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

# C:1



#-------------------------------------
# C:2



#-------------------------------------
# C:3



#-------------------------------------
# C:4



#-------------------------------------
# C:5



#-------------------------------------


# Part D - isinstance()

# D:1



#-------------------------------------
# D:2



#-------------------------------------
# D:3



#-------------------------------------
# D:4



#-------------------------------------
# D:5



#-------------------------------------


# Part E - __str__

# E:1



#-------------------------------------
# E:2



#-------------------------------------
# E:3



#-------------------------------------
# E:4



#-------------------------------------
# E:5



#-------------------------------------


# Part F - __str__ with inheritance

# F:1



#-------------------------------------
# F:2



#-------------------------------------
# F:3



#-------------------------------------
# F:4



#-------------------------------------
# F:5



#-------------------------------------


# Part G - Inheritance or composition?

# G:1



#-------------------------------------
# G:2



#-------------------------------------
# G:3



#-------------------------------------
# G:4



#-------------------------------------
# G:5



#-------------------------------------
# G:6



#-------------------------------------


# Part H - Applied challenge: Export system

# H:1



#-------------------------------------
# H:2



#-------------------------------------
# H:3



#-------------------------------------
# H:4



#-------------------------------------
# H:5



#-------------------------------------
# H:6



#-------------------------------------
# H:7



#-------------------------------------
# H:8



#-------------------------------------
# H:9



#-------------------------------------
# H:10