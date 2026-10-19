
# Smart Plant Monitoring System

## Project Overview
This project uses three algorithms to monitor plant conditions:
1. Hidden Markov Model (HMM)
2. Kalman Filter
3. Dynamic Bayesian Network (DBN)

## Problem Statement 1: HMM

A plant monitoring system records soil moisture readings over eight days:
65, 58, 42, 35, 49, 60, 53, 40.

Classify the readings as Wet (55% or above), Medium (45%-54%), or Dry (below 45%).

Initial probabilities:
- P(Healthy) = 0.8
- P(Stressed) = 0.2

Transition probabilities:

| Previous State | Healthy | Stressed |
|---|---:|---:|
| Healthy | 0.85 | 0.15 |
| Stressed | 0.35 | 0.65 |

Emission probabilities:

| State | Wet | Medium | Dry |
|---|---:|---:|---:|
| Healthy | 0.6 | 0.3 | 0.1 |
| Stressed | 0.1 | 0.3 | 0.6 |

**Question:** Implement the HMM using the Viterbi algorithm to determine the most likely hidden plant state for each day.

## Problem Statement 2: Kalman Filter

The soil moisture measurements are:
65, 58, 42, 35, 49, 60, 53, 40.

Initial estimate = 60  
Initial uncertainty P = 10  
Process noise variance Q = 2  
Measurement noise variance R = 9

**Question:** Implement the Kalman Filter to estimate soil moisture for each day and display the final estimate.

## Problem Statement 3: DBN

Soil moisture readings:
65, 58, 42, 35, 49, 60, 53, 40.

Watering status:
False, False, False, True, False, False, False, True.

Initial probability of stress = 0.10.

| Moisture | Healthy to Stressed | Stressed to Stressed |
|---|---:|---:|
| Wet | 0.05 | 0.25 |
| Medium | 0.15 | 0.55 |
| Dry | 0.60 | 0.85 |

When watering occurs, subtract 0.20 from the Healthy-to-Stressed probability and 0.25 from the Stressed-to-Stressed probability, with a minimum of 0.01.

**Question:** Implement a simplified DBN to calculate the probability of plant stress each day. Classify the plant as Stressed if its probability is at least 0.50; otherwise, classify it as Healthy.

## Technologies Used
- Python
- Matplotlib for graphs

## How to Run
Install Matplotlib:

`python -m pip install matplotlib`

Run each program:

`python plant_hmm.py`

`python plant_kalman.py`

`python plant_dbn.py`

## Note
This is an educational project using sample data and illustrative probabilities. The predictions have not been validated against real plant measurements.

