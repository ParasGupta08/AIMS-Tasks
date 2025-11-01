import pandas as pd

data = pd.read_csv("onehotEnc_data.csv")

print("Original Data\n", data)

categorical_col = ["Gender","Department"]

for col in categorical_col:
    unique_val = data[col].unique()
    for value in unique_val:
        new_col = f"{col}_{value}"
        data[new_col] = (data[col] == value).astype(int)
        
print("\nEncoded Data\n",data)  