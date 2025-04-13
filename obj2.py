
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_hospital_dataset.csv")

# Set theme
sns.set_theme(style="whitegrid")

# 1. Most Common Admission Types
plt.figure(figsize=(7, 5))
sns.countplot(
    data=df,
    x='Admission_Type',
    order=df['Admission_Type'].value_counts().index,
    palette='Set2'
)
plt.title("📋 Most Common Types of Admissions", fontsize=14, fontweight='bold')
plt.xlabel("Admission Type")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# 2. Admission Types Across Departments
plt.figure(figsize=(10, 6), constrained_layout=True)
sns.countplot(
    data=df,
    x='Department',
    hue='Admission_Type',
    palette='Set3'
)
plt.title("🏥 Admission Types Across Departments", fontsize=14, fontweight='bold')
plt.xlabel("Department")
plt.ylabel("Number of Admissions")
plt.xticks(rotation=45)
plt.legend(title="Admission Type")
plt.show()

# 3. Stacked Bar Plot (Proportion)
dept_admit = df.groupby(['Department', 'Admission_Type'], observed=True).size().unstack().fillna(0)
dept_admit_pct = dept_admit.div(dept_admit.sum(axis=1), axis=0)

ax = dept_admit_pct.plot(
    kind='bar',
    stacked=True,
    figsize=(10, 6),
    cmap='tab20c'  # Fixed from colormap
)
plt.title("📊 Proportion of Admission Types by Department", fontsize=14, fontweight='bold')
plt.xlabel("Department")
plt.ylabel("Proportion")
plt.legend(title="Admission Type", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

