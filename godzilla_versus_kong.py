budget = float(input())
statist = int(input())
costume_for_one = float(input())

costume_for_all = costume_for_one*statist
deco = budget*0.10

if statist > 150:
    costume_for_all = costume_for_all*0.90

expenditures = costume_for_all + deco
diff = abs(expenditures-budget)

if expenditures > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
