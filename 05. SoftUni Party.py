number_of_guests = int(input())
set_of_invited = set()
set_of_came = set()

for _ in range(number_of_guests):
    invited_guests = input()
    set_of_invited.add(invited_guests)

while True:
    guests_came = input()
    if guests_came == "END":
        break
    set_of_came.add(guests_came)

guests_didnt_come = sorted(set_of_invited - set_of_came)
print(len(guests_didnt_come))
print("\n".join(guests_didnt_come))