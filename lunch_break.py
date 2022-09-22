import math
name_movie = input()
length_one_episode = int(input())
length_break = int(input())

time_for_lunch = length_break/8
time_for_rest = length_break/4
busy_time = time_for_lunch + time_for_rest
pleasure_time = busy_time + length_one_episode
diff_abs = abs(length_break-pleasure_time)
diff = math.ceil(diff_abs)
if length_break >= pleasure_time:
    print(f"You have enough time to watch {name_movie} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_movie}, you need {math.ceil(diff)} more minutes.")