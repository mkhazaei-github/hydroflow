import pandas as pd

# Path to the input file
file_path = "data/Ober-Eschbach_W15min.csv"

# Read CSV
df = pd.read_csv(file_path)

# Show first 5 rows
print(df.head())