class User:
    def __init__(self, first_name, last_name, email, password):
        self.__full_name = first_name + " " + last_name
        self.__email = email
        self.__password = password



    def get_full_name(self):
        return self.__full_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password



    def __str__(self):
        return f'''
        Fullname : {self.__full_name}
        Email : {self.__email}'''

