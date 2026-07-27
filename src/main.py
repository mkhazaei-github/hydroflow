from src.reader import read_csv

file_path = "data/Ober-Eschbach_W15min.csv"

df = read_csv(file_path)

print(df.head())