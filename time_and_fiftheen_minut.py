hours = int(input())
minutes = int(input())
times = hours*60 + minutes
how_is_time_after_fifteen_minutes = times + 15

hours = how_is_time_after_fifteen_minutes // 60
minutes = how_is_time_after_fifteen_minutes % 60

if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")


