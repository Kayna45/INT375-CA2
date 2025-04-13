import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_hospital_dataset.csv")

# Set the visual style
sns.set(style="whitegrid")

# Create a boxplot to examine length of stay by department
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Department', y='Length_of_Stay', palette='Set2')
plt.title("Length of Stay Across Departments")
plt.xlabel("Department")
plt.ylabel("Length of Stay (days)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
