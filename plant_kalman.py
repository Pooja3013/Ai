# SMART PLANT MONITORING USING KALMAN FILTER

import matplotlib.pyplot as plt

# Input: noisy soil moisture measurements (%)
measurements = [65, 58, 42, 35, 49, 60, 53, 40]

# Initial estimate and uncertainty
estimate = 60.0
P = 10.0

# Noise variances
Q = 2.0
R = 9.0

# Store estimates for plotting
estimates = []

print("SMART PLANT MONITORING - KALMAN FILTER")
print("-" * 55)
print("Day | Measurement | Estimated Moisture")
print("-" * 55)

for day, z in enumerate(measurements, start=1):

    # Step 1: Predict the next moisture estimate
    predicted_estimate = estimate
    predicted_P = P + Q

    # Step 2: Calculate Kalman Gain
    K = predicted_P / (predicted_P + R)

    # Step 3: Correct estimate using the measurement
    estimate = predicted_estimate + K * (
        z - predicted_estimate
    )

    # Step 4: Update estimate uncertainty
    P = (1 - K) * predicted_P

    # Save the estimate
    estimates.append(estimate)

    print(
        f"{day:3} | {z:11.2f}% | {estimate:18.2f}%"
    )

print("-" * 55)
print(f"Final estimated moisture: {estimate:.2f}%")

# Graph: measurements vs estimated moisture
days = range(1, len(measurements) + 1)

plt.figure(figsize=(9, 5))

plt.plot(
    days,
    measurements,
    marker="o",
    linestyle="--",
    label="Sensor Moisture"
)

plt.plot(
    days,
    estimates,
    marker="s",
    linestyle="-",
    label="Kalman Estimated Moisture"
)

plt.xlabel("Day")
plt.ylabel("Soil Moisture (%)")
plt.title("Kalman Filter - Soil Moisture Estimation")
plt.xticks(list(days))
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
