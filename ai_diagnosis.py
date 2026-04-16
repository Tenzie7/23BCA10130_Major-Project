import pandas as pd
import random

# Simulated AI predictions
data = []

for i in range(1, 21):
    actual = random.choice(["Normal", "Pneumonia"])
    predicted = random.choice(["Normal", "Pneumonia"])
    confidence = round(random.uniform(0.7, 0.98), 2)

    data.append([f"Image_{i}", actual, predicted, confidence])

df = pd.DataFrame(data, columns=["Image", "Actual", "Predicted", "Confidence"])

df.to_csv("results.csv", index=False)

print("✅ AI Diagnosis Results Generated!")