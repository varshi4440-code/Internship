import random
print(" INDEPENDENT EVENTS ")
P_heads =1/2
P_six = 1/6
P_both_independent = P_heads * P_six

print("Probability of heads AND rolling a 6:", P_both_independent)
print("\n----- DEPENDENT EVENTS(WITHOUT REPLACEMENT) -----")

red = 5
blue = 5
total = red + blue

P_first_red = red / total
P_second_red = (red-1) / (total -1)
P_both_red = P_first_red * P_second_red

print("Theoritical Probability (Both Red):", P_both_red)

print("\n----- SIMULATION (EXPERIMENTAL PROBABILITY) -----")

trials = 10000
count_both_red = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5
    pick = random.sample(bag, 2)  # without replacement
    
    if pick[0] == "R" and pick[1] == "R":
        count_both_red += 1

experimental_probability = count_both_red / trials

print("Experimental Probability (Both Red):", experimental_probability)

print("\nNote: The experimental probability should be close to 2/9 =", 2/9)