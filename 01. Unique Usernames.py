count_usernames = int(input())
set_unique_users = set()
for _ in range(count_usernames):
    username = input()
    set_unique_users.add(username)
print("\n".join(set_unique_users))
