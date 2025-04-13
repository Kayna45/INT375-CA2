import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_hospital_dataset.csv")

# Set the visual style
sns.set(style="whitegrid")

# 1. Distribution of Satisfaction Scores
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Satisfaction_Score', palette='coolwarm')
plt.title("Distribution of Patient Satisfaction Scores")
plt.xlabel("Satisfaction Score")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# 2. Satisfaction by Department
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Department', y='Satisfaction_Score', palette='Set3')
plt.title("Patient Satisfaction Scores by Department")
plt.xlabel("Department")
plt.ylabel("Satisfaction Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Satisfaction by Admission Type
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Admission_Type', y='Satisfaction_Score', palette='Set2')
plt.title("Satisfaction Score by Admission Type")
plt.xlabel("Admission Type")
plt.ylabel("Satisfaction Score")
plt.tight_layout()
plt.show()
