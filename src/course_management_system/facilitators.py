class Facilitators:
    def __init__(self,name,email_addresss):
        self.name = name
        self.email_addresss = email_addresss

    def register_facilitator(self,name,email_addresss):
        if name and email_addresss:
            return "You've been registered successfully"
        if name == "":
            raise TypeError("Name cannot be empty")
        if email_addresss == "":
            raise TypeError("Email Address cannot be empty")

    def log_in(self,name,email_addresss):
        if name and email_addresss:
            return "You've been logged in"
        if name == "":
            raise TypeError("Name cannot be empty")
        if email_addresss == "":
            raise TypeError("Email Address cannot be empty")


