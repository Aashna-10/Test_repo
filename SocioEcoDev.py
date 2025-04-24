import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Load the CSV file into a DataFrame
infra_df = pd.read_csv("Socio-EcoDev.csv")


# Load your cleaned DataFrame (infra_df) with 4 columns
cols = [
    'no_of_households_receiving_benefits_under_pmksn',
'total_no_of_farmers_registered_under_pmkpy',
'total_no_of_farmers_received_benefit_under_pmkpy'
]



# Step 1: Standardize
scaler = StandardScaler()
infra_scaled = scaler.fit_transform(infra_df[cols])

# Step 2: PCA
pca = PCA()
components = pca.fit_transform(infra_scaled)

# Step 3: Use the first component as index
infra_df["SocioEcoDev_Index"] = components[:, 0]

# Step 4: Get weights (PC1 loadings)
weights = pd.DataFrame(pca.components_[0], index=cols, columns=["PC1_Loading"])

print("Explained Variance (Top 3 Components):", pca.explained_variance_ratio_[:3])
print("Weights for each variable:\n", weights)
print("Sample Index:\n", infra_df[["SocioEcoDev_Index"]])
infra_df.to_csv("SocioEcoDev_with_index.csv", index=False)

