
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("cleaned_hospital_dataset.csv")

# Add Age Groups
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 18, 35, 60, 100],
                         labels=['0-18', '19-35', '36-60', '60+'])

# Set theme
sns.set_theme(style="whitegrid")

# 1. Pie Chart: Gender Distribution
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, 
        colors=sns.color_palette("pastel"))
plt.title("Gender Distribution of Patients")
plt.axis('equal')
plt.tight_layout()
plt.show()

# 2. Histogram: Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=30, kde=True, color='teal')
plt.title("Patient Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# 3. Count Plot: Admission Type by Gender
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Admission_Type', hue='Gender', palette='coolwarm')
plt.title("Admission Types by Gender")
plt.xlabel("Admission Type")
plt.ylabel("Count")
plt.legend(title="Gender")
plt.tight_layout()
plt.show()

# 4. Count Plot: Treatment Plan by Gender
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Treatment_Plan', hue='Gender', palette='Set3')
plt.title("Treatment Plans by Gender")
plt.xlabel("Treatment Plan")
plt.ylabel("Count")
plt.legend(title="Gender")
plt.tight_layout()
plt.show()

# 5.Stacked Bar Chart: Treatment Plan by Age Group
treatment_by_age = pd.crosstab(df['Age_Group'], df['Treatment_Plan'])

treatment_by_age.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Accent')
plt.title("Treatment Plans by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Patients")
plt.legend(title="Treatment Plan")
plt.tight_layout()
plt.show()

# 6.

plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, fmt=".2f", cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 7. 🔵 Optional: Scatter Plot (Age vs Length of Stay)
if 'Length_of_Stay' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='Age', y='Length_of_Stay', hue='Gender', palette='Set1')
    plt.title("Age vs Length of Stay")
    plt.xlabel("Age")
    plt.ylabel("Length of Stay")
    plt.tight_layout()
    plt.show()

