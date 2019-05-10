class Password:

    password_list = []

    def save_password(self):
            Password.password_list.append(self)

    def delete_contact(self):
            Password.password_list.remove(self)


    def __init__(self,first_name,last_name,user_name,password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password