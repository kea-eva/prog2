class UserInfo:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def validate_password(self, password):
        return password == self.__password

    def change_password(self, current_password, new_password):
        if self.validate_password(current_password):
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect current password.")

# Creating a user
user = UserInfo("alice", "securepassword")

# Accessing private variable (do NOT do like this!!)
print(user._UserInfo__password)

# Using methods to interact with private variables
user.change_password("incorrect", "newpassword")
user.change_password("securepassword", "newpassword")
