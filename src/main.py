import pandas as pd

print("HydroFlow started successfully!")

data = {
    "Station": ["Eschbach", "Schwarzbach"],
    "Discharge": [12.4, 8.7]
}

df = pd.DataFrame(data)

print(df)

def add(a, b):
    return a + b


print(add(5, 3))
