import sys

# def rozwiazanie_pierwsze():
user_login = {}
user_total_time = {}

file_name = "nwm/logs.txt"

with open(file_name) as f:
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
            user_total_time[user] = user_total_time.get(user, 0) + time - user_login[user]

print("Czas spędzony w systemie przez użytkownika: ")
for user, time in user_total_time.items():
    print(f" - {user}: {time} s.")

# for user, time in sorted(user_total_time, key=lambda x: x[1], reverse=True):
#     print(f" - {user}: {time} s.")




    # def rozwiazanie_drugie():
    #     user_login = {}
    #     user_total_time = {}
    #
    #     file_name = "nwm/logs.txt"
    #
    #     with open(file_name) as f:
    #         for line in f:
    #             line = line.split(";")
    #             user = line[0]
    #             action = line[1]
    #             time = line[2]
    #             time = int(time)
    #
    #             # print(line, time)
    #
    #             if action == "LOGIN":
    #                 user_login[user] = time
    #             if action == "LOGOUT":
    #                 user_total_time[user] = user_total_time.get(user, 0) + time - user_login[user]
    #
    #
    # print("Czas spędzony w systemie przez użytkownika: ")
    # for user, time in user_total_time.items():
    #     print(f" - {user}: {time} s.")
    #
    # for user, time in sorted(user_total_time)