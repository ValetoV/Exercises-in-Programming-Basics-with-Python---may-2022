n1 = int(input())
n2 = int(input())
operator = input()
action = 0
odd_or_even = ""
is_zero = False

if operator == "+":
    action = n1 + n2

elif operator == "-":
    action = n1 - n2

elif operator == "*":
    action = n1 * n2

elif operator == "/":
    if n2 == 0:
        is_zero = True
    else:
        action = n1 / n2
elif operator == "%":
    if n2 == 0:
        is_zero = True
    else:
        action = n1 % n2

if is_zero:
    print(f"Cannot divide {n1} by zero")

elif operator == "+" or operator == "-" or operator == "*":
    if action % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{n1} {operator} {n2} = {action} - {odd_or_even}")

elif operator == "/":
    print(f"{n1} {operator} {n2} = {action:.2f}")

else:
    print(f"{n1} {operator} {n2} = {action}")