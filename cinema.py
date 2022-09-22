type_tickets = input()
count_rows = int(input())
count_columns = int(input())

cinema_capacity = count_rows * count_columns
income = 0

if type_tickets == "Premiere":
   income = cinema_capacity * 12
elif type_tickets == "Normal":
    income = cinema_capacity * 7.50
elif type_tickets == "Discount":
    income = cinema_capacity * 5.00

print (f"{income:.2f}")
print("leva")