import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_hospital_dataset.csv")

# Set the visual style
sns.set(style="whitegrid")

# 1. Calculate readmission rate (%) per room type
readmission_rate = df.groupby("Room_Type")["Readmission_Within_30_Days"].mean().reset_index()
readmission_rate["Readmission_Within_30_Days"] *= 100  # Convert to percentage

# 2. Plot the readmission rate by room type
plt.figure(figsize=(8, 5))
sns.barplot(data=readmission_rate, x="Room_Type", y="Readmission_Within_30_Days", palette="Set2")
plt.title("Readmission Rate Within 30 Days by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Readmission Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
