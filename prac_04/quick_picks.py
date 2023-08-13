import random

num_quick_picks = int(input("How many quick picks? "))

for i in range(num_quick_picks):
    quick_pick = sorted(random.sample(range(1, 46), 6))
    print(" ".join(str(num) for num in quick_pick))