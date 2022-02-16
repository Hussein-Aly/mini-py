
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("123","hussein")
user2 = User("456","hamza")

user1.follow(user2)

print(user1.following, user1.followers)
print(user2.following, user2.followers)
