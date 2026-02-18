import itertools

actions = ["Click", "Scroll", "Exit"]

# Generate sample space
sample_space = list(itertools.product(actions, repeat=2))

# Event: at least one Click
event = [outcome for outcome in sample_space if "Click" in outcome]

probability = len(event) / len(sample_space)

print("Sample Space:", sample_space)
print("Total Outcomes:", len(sample_space))
print("Favorable Outcomes:", len(event))
print("Probability of at least one Click:", probability)
