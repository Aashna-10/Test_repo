import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Load the CSV file into a DataFrame
infra_df = pd.read_csv("RuralInfra.csv")


# Load your cleaned DataFrame (infra_df) with 4 columns
cols = [
    'availability_of_food_storage_warehouse', 
    'is_broadband_available',
    'is_bank_buss_correspondent_with_internet',
    'availability_of_telephone_services',
    'availability_of_market',
    'distance_of_market',
    'availability_of_public_transport'
]



# Step 1: Standardize
scaler = StandardScaler()
infra_scaled = scaler.fit_transform(infra_df[cols])

# Step 2: PCA
pca = PCA()
components = pca.fit_transform(infra_scaled)

# Step 3: Use the first component as index
infra_df["RuralInfrastructure_Index"] = components[:, 0]

# Step 4: Get weights (PC1 loadings)
weights = pd.DataFrame(pca.components_[0], index=cols, columns=["PC1_Loading"])

print("Explained Variance (Top 3 Components):", pca.explained_variance_ratio_[:3])
print("Weights for each variable:\n", weights)
print("Sample Index:\n", infra_df[["RuralInfrastructure_Index"]].head())
infra_df.to_csv("RuralInfra_with_index.csv", index=False)
