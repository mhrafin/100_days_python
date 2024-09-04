class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user_followed):
        user_followed.followers += 1
        self.following += 1


user_1 = User("001", "Rafin")
user_2 = User("002", "Andrew Tate")

user_2.follow(user_1)  # User 2 followed user 1 XD

# Now lets see everyone's follow stats
print(f"User 1 {user_1.username} is following {user_1.following} people.")
print(f"User 1 {user_1.username} is followed by {user_1.followers} people.")

print(f"User 2 {user_2.username} is following {user_2.following} people.")
print(f"User 2 {user_2.username} is followed by {user_2.followers} people.")