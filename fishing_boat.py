budget = int(input())
season = input()
count_fisherman = int(input())
rent=0

if season == "Spring":
    rent = 3000
    if count_fisherman <= 6:
        rent = rent * 0.90
    elif 7 <= count_fisherman <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75
        if count_fisherman % 2 == 0:
          rent = rent * 0.95

elif season == "Summer" or season == "Autumn":
    rent = 4200
    if count_fisherman <= 6:
        rent = rent * 0.90
    elif 7 <= count_fisherman <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75

if count_fisherman % 2 == 0:
    if season != "Autumn":
        rent = rent * 0.95

elif season == 'Winter':
    rent = 2600
    if count_fisherman <= 6:
        rent = rent * 0.90
    elif 7 <= count_fisherman <= 11:
        rent = rent * 0.85
    else:
        rent = rent * 0.75

if count_fisherman % 2 == 0:
    if season != "Autumn":
        rent = rent * 0.95

diff = abs(budget - rent)
if budget <= rent:
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    print(f"Yes! You have {diff:.2f} leva left.")
