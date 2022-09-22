hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

time_min_exam = (hour_exam * 60) + minutes_exam
time_min_arrival = (hour_arrival * 60) + minutes_arrival
diff = abs(time_min_exam - time_min_arrival)

if time_min_arrival > time_min_exam:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hour = diff // 60
        min = diff % 60
        if min < 10:
            print(f"{hour}:0{min} hours after the start")
        else:
            print(f"{hour}:{min} hours after the start")

elif time_min_arrival == time_min_exam or diff <= 30:
    print("On time")
    if 1 <= diff <= 30:
        print(f"{diff} minutes before the start")
else:
    print("Early")

    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        hour = diff // 60
        min = diff % 60
        if min < 10:
            print(f"{hour}:0{min} hours before the start")
        else:
            print(f"{hour}:{min} hours before the start")