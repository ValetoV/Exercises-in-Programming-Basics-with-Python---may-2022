trip = float(input())
puzzles = int(input())
dolls = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

price_puzzles = puzzles * 2.60
price_dolls = dolls * 3
price_bear = bear * 4.10
price_minion = minion * 8.20
price_truck = truck * 2

price_all = price_puzzles + price_dolls + price_bear + price_minion + price_truck
count_all = puzzles + dolls + bear + minion + truck

#if count_all >= 50:
#    price_all = price_all * 0.75

#price_all = price_all - (price_all * 0.10)
#left = abs(price_all - trip)

#if trip <= price_all:
#   print(f'Yes! {left:.2f} lv left.')
#else:
#    print(f'Not enough money! {left:.2f} lv needed.')
#редове 17-20 ги триеш и заместваш с
#if count_all >= 50:
#price_all = price_all * 0.75
#ред 25 заместваш с:
#if trip <= price_all:

if count_all >= 50:
    price_all = price_all - (price_all * 0.25)

price_all = price_all - (price_all * 0.10)
left = abs(price_all - trip)

if trip <= price_all:
    print(f"Yes! {left:.2f} lv left.")
else:
    print(f"Not enough money! {left:.2f} lv needed.")