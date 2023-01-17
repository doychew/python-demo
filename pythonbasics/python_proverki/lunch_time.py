import math
name_of_serial = input()
time_of_episode = int(input())
time_of_break = int(input())

time_for_lunch = time_of_break *1/8
time_for_rest = time_of_break * 1/4
time_left = time_of_break - time_for_lunch - time_for_rest
if time_left >= time_of_episode:
    print(f"You have enough time to watch {name_of_serial} and left with {math.ceil(time_left - time_of_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {math.ceil(time_of_episode - time_left)} more minutes.")