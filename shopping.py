budget = float(input())
video_card = int(input())
cpu = int(input())
ram_memory = int(input())

price_video_card = video_card * 250
price_cpu = cpu * (price_video_card * 0.35)
price_ram_memory = ram_memory * (price_video_card * 0.10)

price = price_video_card + price_cpu + price_ram_memory

if video_card > cpu:
    price = price * 0.85

diff = abs(budget - price)

if price <= budget:
      print(f"You have {diff:.2f} leva left!")
else:
      print(f"Not enough money! You need {diff:.2f} leva more!")