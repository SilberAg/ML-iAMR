import pandas as pd
data = pd.read_csv("example_file\example_data.csv")
pheno = pd.read_csv("example_file\example_pheno.csv")

print(data.head())
print(data.shape)
