import pandas as pd

data = pd.read_csv("imputationEnc_data.csv")

missing_data_cols = ["Salary","Experience","Score", "Age"]

print("Original Data\n",data)

x = int(input("What Imputation Tec To use:\nFor Mean Enter 1\nFor Median Enter 2\nFor Mode Enter 3\n"))


# Mean 
if (x==1):
    for col in missing_data_cols:
        total_sum = 0
        count = 0
        for i in range(len(data)):
            if not (pd.isna(data.loc[i,col])):
                total_sum += data.loc[i,col]
                count += 1

        mean = total_sum/count
        
        for i in range(len(data)):
            if (pd.isna(data.loc[i,col])):
                data.loc[i,col] = mean
    
    print("\nMean Imputed Data\n", data)       
     
# Median
elif (x == 2):
    for col in missing_data_cols:
        values = []
        for i in range(len(data)):
            if not (pd.isna(data.loc[i,col])):
                values.append(data.loc[i,col])
        values.sort()
        length = len(values)
        median = 0
        if length % 2 == 1:
            median = values[length // 2]   
        else:
            median = (values[(length // 2) - 1] + values[length // 2]) / 2 
        
        for i in range(len(data)):
            if (pd.isna(data.loc[i,col])):
                data.loc[i,col] = median
    print("\nMedian Imputed Data\n", data)    
    
# Mode  
elif (x == 3):
    for col in  missing_data_cols:
        values = []
        for i in range(len(data)):
            if not (pd.isna(data.loc[i, col])):
                values.append(data.loc[i,col])
            
        freq= {}
        
        for val in values:
            if val in freq:
                freq[val] += 1
                
            else :
                freq[val] = 1
                
        count = 0
        mode = 0
        for key in freq:
            if freq[key] > count:
                count = freq[key]
                mode = key
                
        for i in range(len(data)):
            if (pd.isna(data.loc[i,col])):
                data.loc[i,col] = mode
                
    print("\nMode Imputed Data\n", data)                  
else : 
    print("Wrong input only 1, 2 or 3 is allowed as input ")
    
    