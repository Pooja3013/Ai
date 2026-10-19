# SMART PLANT MONITORING USING HMM
# Hidden Markov Model with Viterbi Algorithm
import matplotlib.pyplot as plt
# Input data: soil moisture readings for 8 days
moisture = [65, 58, 42, 35, 49, 60, 53, 40]

# Convert moisture readings into observations
def get_category(value):
    if value >= 55:
        return "Wet"
    elif value >= 45:
        return "Medium"
    else:
        return "Dry"

observations = [get_category(x) for x in moisture]

states = ["Healthy", "Stressed"]

# Initial probabilities
initial = {
    "Healthy": 0.8,
    "Stressed": 0.2
}

# Transition probabilities
transition = {
    "Healthy": {"Healthy": 0.85, "Stressed": 0.15},
    "Stressed": {"Healthy": 0.35, "Stressed": 0.65}
}

# Emission probabilities
emission = {
    "Healthy": {"Wet": 0.6, "Medium": 0.3, "Dry": 0.1},
    "Stressed": {"Wet": 0.1, "Medium": 0.3, "Dry": 0.6}
}

# Viterbi initialization
V = [{}]
path = {}

for state in states:
    V[0][state] = (
        initial[state] * emission[state][observations[0]]
    )
    path[state] = [state]

# Viterbi recursion
for t in range(1, len(observations)):
    V.append({})
    new_path = {}

    for current in states:
        probability, previous = max(
            (
                V[t - 1][prev]
                * transition[prev][current]
                * emission[current][observations[t]],
                prev
            )
            for prev in states
        )

        V[t][current] = probability
        new_path[current] = path[previous] + [current]

    path = new_path

# Find the most likely hidden-state sequence
last_state = max(states, key=lambda s: V[-1][s])
best_path = path[last_state]

# Display results
print("SMART PLANT MONITORING - HMM")
print("-" * 55)

for day, (value, observation, state) in enumerate(
    zip(moisture, observations, best_path), start=1
):
    print(
        f"Day {day}: Moisture={value}% | "
        f"Observation={observation} | Predicted state={state}"
    )

print("-" * 55)
print("Most likely hidden-state sequence:")
print(" -> ".join(best_path))

# Graph: predicted plant state
state_values = [
    0 if state == "Healthy" else 1
    for state in best_path
]

plt.figure(figsize=(9, 5))
plt.step(
    range(1, len(best_path) + 1),
    state_values,
    where="mid",
    marker="o"
)

plt.yticks([0, 1], ["Healthy", "Stressed"])
plt.xticks(range(1, len(best_path) + 1))
plt.xlabel("Day")
plt.ylabel("Predicted Plant State")
plt.title("HMM - Plant Health Prediction")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
