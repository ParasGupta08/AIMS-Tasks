import pandas as pd

data = pd.read_csv("onehotEnc_data.csv")

print("Original Data\n", data)

categorical_col = ["Gender","Department"]

for col in categorical_col:
    unique_val = data[col].unique()
    for value in unique_val:
        new_col = f"{col}_{value}"
        data[new_col] = 0
        
    for i in range(len(data)):
        update_col = f"{col}_{data.loc[i][col]}"
        data.loc[i, update_col] = 1
    
print("\nEncoded Data\n",data)