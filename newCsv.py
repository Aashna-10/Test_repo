# Import the index DataFrames from the three scripts
from RuralInfra import infra_df     # contains RuralInfrastructure_Index
from pca import infra_df       # contains AgriProd_Index
from SocioEcoDev import infra_df     # contains SocioEcoDev_Index

# Combine the three index columns
final_df = RuralInfra.infra_df[["RuralInfrastructure_Index"]].copy()
final_df["AgriProd_Index"] = pca.infra_df["AgriProd_Index"]
final_df["SocioEcoDev_Index"] = SocioEcoDev.infra_df["SocioEcoDev_Index"]

# Save to CSV
final_df.to_csv("final_composite_indices.csv", index=False)

print("CSV created successfully with all 3 indices!")
