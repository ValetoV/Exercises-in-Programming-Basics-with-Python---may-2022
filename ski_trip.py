day_of_stay = int(input())
type_of_room = input()
assessment = input()

price = 0
nights = day_of_stay - 1

if type_of_room == "room for one person":
    price = 18 * nights
elif type_of_room == "apartment":
    price = 25 * nights
    if day_of_stay < 10:
        price = price * 0.70
    elif 10 < day_of_stay < 15:
        price = price * 0.65
    else:
        price = price * 0.50
elif type_of_room == "president apartment":
    price = 35 * nights
    if day_of_stay < 10:
        price = price * 0.90
    elif 10 < day_of_stay < 15:
        price = price * 0.85
    else:
        price = price * 0.80

if assessment == "positive":
    price = price * 1.25
else:
    price = price * 0.90

print(f"{price:.2f}")
