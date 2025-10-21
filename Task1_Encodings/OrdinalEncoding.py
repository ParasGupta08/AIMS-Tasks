git cimport pandas as pd

data = pd.read_csv("ordinalEnc_data.csv")
print("Original Data\n" ,data)

educationMap = {
    "High School" : 0,
    "Bachelor" : 1,
    "Master" : 2,
    "PhD" : 3
    }

expMap = {
    "Junior" : 0,
    "Mid" : 1,
    "Senior" : 2,
    "Expert" : 3
    }

sizeMap = {
    "Small" : 0 ,
    "Medium" :1 ,
    "Large" : 2  
}

def OrdinalEncoder(Column, Map) :
    newColumn = f"{Column}_Encoded"
    for value in data[Column]:
        data[newColumn] = data[Column].map(Map)
    
Education_Level = "Education_Level"
Experience_Level = "Experience_Level"
Company_Size = "Company_Size"
OrdinalEncoder(Education_Level, educationMap)
OrdinalEncoder(Experience_Level, expMap)
OrdinalEncoder(Company_Size, sizeMap)

print("\nEncoded Data\n" , data)
    
    
    



