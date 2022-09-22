budget = float(input())
season = input()

destination = ""
type_of_stay = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_stay = "Camp"
        price = budget * 0.30

    elif season == "winter":
        type_of_stay = "Hotel"
        price = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_stay = "Camp"
        price = budget * 0.40
    elif season == "winter":
        type_of_stay = "Hotel"
        price = budget * 0.80

else:
    destination = "Europe"
    type_of_stay = "Hotel"
    price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type_of_stay} - {price:.2f}")