from persistent import Persistent

class Contact(Persistent):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def update(self, phone=None, email=None):
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def __repr__(self):
        return f"<Contact name={self.name}, phone={self.phone}, email={self.email}>"
