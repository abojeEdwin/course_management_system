class Facilitators:
    def __init__(self,name,email_address):
        self.name = name
        self.email_address = email_address

    def register_facilitator(self,name,email_address):
        if name and email_address:
            return "You've been registered successfully"
        if name == "":
            raise TypeError("Name cannot be empty")
        if email_address == "":
            raise TypeError("Email Address cannot be empty")

    def log_in(self,name,email_address):
        if name and email_address:
            return "You've been logged in"
        if name == "":
            raise TypeError("Name cannot be empty")
        if email_address == "":
            raise TypeError("Email Address cannot be empty")


