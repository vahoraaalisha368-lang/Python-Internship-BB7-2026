users = ["alisha", "aaysha", "cakeberry", "aris", "priya"]
long_users = list(filter(lambda u: len(u) >= 6, users))
print(long_users)  