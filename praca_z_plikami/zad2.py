import sys

user_login = {}
user_logout = {}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.split(";")
        user = line[0]
        action = line[1]
        time = line[2]
        time = int(time)

        # print(line, time)

        if action == "LOGIN":
            user_login[user] = time
        if action == "LOGOUT":
            user_logout[user] = user_logout.get(user, 0) + time - user_login[user]

print("Czas spędzony w systemie przez użytkownika: ")
# for i in sorted(user_login.items(), key=lambda x: x[1],reverse=True):
#     print(i)
print(f"{user_logout}")