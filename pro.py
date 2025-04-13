import pandas as pd

# Load the dataset
df = pd.read_csv("hospital_system_dataset.csv")

# Step 1: Drop unnecessary ID columns
df_cleaned = df.drop(columns=["Patient_ID", "Doctor_ID", "Nurse_ID"])

# Step 2: Standardize categorical string columns (strip spaces, capitalize properly)
categorical_cols = df_cleaned.select_dtypes(include="object").columns
for col in categorical_cols:
    df_cleaned[col] = df_cleaned[col].str.strip().str.title()

# Step 3: Check for outliers (optional view)
print("Numerical Summary:\n")
print(df_cleaned.describe())

# Step 4: Confirm cleaned categories (optional view)
print("\nUnique Values in Categorical Columns:\n")
for col in categorical_cols:
    print(f"{col}: {df_cleaned[col].unique()}")

# Optional: Save the cleaned dataset
df_cleaned.to_csv("cleaned_hospital_dataset.csv", index=False)
