world_record = float(input())
distance = float(input())
time_for_one_meter = float(input())

resistance = (distance//15) * 12.5
time_ivan = (distance * time_for_one_meter) + resistance
diff = time_ivan - world_record
if time_ivan < world_record:
    print(f"Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")