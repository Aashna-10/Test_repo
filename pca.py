import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Load the CSV file into a DataFrame
infra_df = pd.read_csv("AgriculturalProd.csv")


# Load your cleaned DataFrame (infra_df) with 4 columns
cols = [
    'availability_of_rain_harvest_system',
    'availability_of_major_source_of_irrigation',
    'total_no_of_rainwater_harvesting_structure',
    'availability_of_custom_hiring_centre_agri_equipment',
    'is_govt_seed_centre_available',
    'is_soil_testing_centre_available'
]



# Step 1: Standardize
scaler = StandardScaler()
infra_scaled = scaler.fit_transform(infra_df[cols])

# Step 2: PCA
pca = PCA()
components = pca.fit_transform(infra_scaled)

# Step 3: Use the first component as index
infra_df["AgriProd_Index"] = components[:, 0]

# Step 4: Get weights (PC1 loadings)
weights = pd.DataFrame(pca.components_[0], index=cols, columns=["PC1_Loading"])

print("Explained Variance (Top 3 Components):", pca.explained_variance_ratio_[:3])
print("Weights for each variable:\n", weights)
print("Sample Index:\n", infra_df[["AgriProd_Index"]].head())

# Assuming you already added the index column like this:
#infra_df["AgriProd_Index"] = components[:, 0]

# Save the updated DataFrame back to CSV
infra_df.to_csv("PCA_with_index.csv", index=False)


