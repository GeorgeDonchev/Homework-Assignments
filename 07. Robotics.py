from collections import deque
from datetime import datetime, timedelta
robots_details = input().split(";")
details = deque()
start_time = datetime.strptime(input(), "%H:%M:%S")
robots = {}

command = input()
while not command == "End":
    detail = command
    details.append(detail)
    command = input()

for robot in robots_details:
    robot_name, robot_proses_time = robot.split("-")
    robots[robot_name] = []
    robots[robot_name].append(int(robot_proses_time))
    robots[robot_name].append(0)

start_new_prosessing_time = 0

while details:
    current_detail = details.popleft()
    start_new_prosessing_time += 1
    for robot in robots.keys():
        if robots[robot][1] <= start_new_prosessing_time:
            robots[robot][1] = start_new_prosessing_time+robots[robot][0]
            # second = robots[robot][0]
            time_str = (start_time + timedelta(seconds = start_new_prosessing_time)).strftime("%H:%M:%S")
            print(f"{robot} - {current_detail} [{time_str}]")
            break
    else:
        details.append(current_detail)