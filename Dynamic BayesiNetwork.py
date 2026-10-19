
# SMART PLANT MONITORING USING A SIMPLIFIED DBN

import matplotlib.pyplot as plt

# Input data
moisture = [65, 58, 42, 35, 49, 60, 53, 40]
watered = [
    False, False, False, True,
    False, False, False, True
]

def get_category(value):
    if value >= 55:
        return "Wet"
    elif value >= 45:
        return "Medium"
    else:
        return "Dry"

# Initial probability of plant stress
p_stressed = 0.10

# Conditional transition probabilities
healthy_to_stressed = {
    "Wet": 0.05,
    "Medium": 0.15,
    "Dry": 0.60
}

stressed_to_stressed = {
    "Wet": 0.25,
    "Medium": 0.55,
    "Dry": 0.85
}

# Store probabilities for plotting
stress_probs = []

print("SMART PLANT MONITORING - DBN")
print("-" * 65)
print("Day | Moisture | Watered | P(Stressed) | Predicted condition")
print("-" * 65)

for day, (value, was_watered) in enumerate(
    zip(moisture, watered), start=1
):
    category = get_category(value)

    # Get transition probabilities for this moisture category
    p_h_to_s = healthy_to_stressed[category]
    p_s_to_s = stressed_to_stressed[category]

    # Adjust probabilities when watering occurs
    if was_watered:
        p_h_to_s = max(0.01, p_h_to_s - 0.20)
        p_s_to_s = max(0.01, p_s_to_s - 0.25)

    # Update probability of stress
    p_stressed = (
        (1 - p_stressed) * p_h_to_s
        + p_stressed * p_s_to_s
    )

    # Save probability for plotting
    stress_probs.append(p_stressed)

    condition = (
        "Stressed" if p_stressed >= 0.50 else "Healthy"
    )

    print(
        f"{day:3} | {value:6}%  | "
        f"{str(was_watered):7} | "
        f"{p_stressed:11.4f} | {condition}"
    )

print("-" * 65)
print(f"Final probability of stress: {p_stressed:.4f}")

# Graph: probability of plant stress
days = range(1, len(moisture) + 1)

plt.figure(figsize=(9, 5))

plt.plot(
    days,
    stress_probs,
    marker="o",
    linestyle="-",
    label="Probability of Stress"
)

plt.axhline(
    y=0.50,
    linestyle="--",
    label="Stress Threshold (0.50)"
)

plt.xlabel("Day")
plt.ylabel("Probability of Stress")
plt.title("DBN - Plant Stress Probability")
plt.xticks(list(days))
plt.ylim(0, 1)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
