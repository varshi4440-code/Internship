import random

trials = 1000
count_sum7 = 0

for _ in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count_sum7 += 1

experimental_probability = count_sum7 / trials

print("Experimental Probability of sum = 7:", experimental_probability)
print("Theoretical Probability:", 1/6)
