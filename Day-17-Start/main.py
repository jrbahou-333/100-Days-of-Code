class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


user_1 = User("001", "Jimbo")


print(user_1.user_id)