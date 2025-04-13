import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_hospital_dataset.csv")

# Set the visual style
sns.set(style="white")

# Select only relevant numeric columns for correlation
numeric_cols = ['Age', 'Length_of_Stay', 'Readmission_Within_30_Days', 'Satisfaction_Score']
correlation_matrix = df[numeric_cols].corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Key Numeric Features")
plt.tight_layout()
plt.show()
