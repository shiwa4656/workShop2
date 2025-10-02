#! C:\Users\shirw\OneDrive\Documents\Practise\workShop2\workshop\Scripts\python.exe
import numpy as np
import pandas as pd

# 1) How many missing Ages?
titanic_csv = pd.read_csv('data/titanic.csv')
missing_age = titanic_csv['Age'].isna().sum()
print(f"Missing Age count: {missing_age}") #177

# 2) Average age (three ways)

mean_pandas = titanic_csv['Age'].mean()
print(mean_pandas)#29.7

mean_np = np.mean(titanic_csv['Age'].to_numpy())
print(mean_np) #Nan
mean_np_nn = np.nanmean(titanic_csv['Age'].to_numpy())
print(mean_np_nn) #29.7

# 3) Replace missing Age with rounded mean (demo; not best practice in real work)

age_fill = int(round(mean_pandas))
titanic_csv["Age"] = titanic_csv["Age"].fillna(age_fill)

# 4) Convert Age to integer type
titanic_csv["Age"] = titanic_csv["Age"].astype("int64")           
# 5) Create dummy "Female" (1 if Sex == 'female', else 0) and drop original Sex
titanic_csv["Female"] = (titanic_csv["Sex"] == "female").astype("int8")  
df = titanic_csv.drop(columns=["Sex"])

# 6) Save cleaned data (comma-separated, no index)
out_path = "titanic-clean.csv"
titanic_csv.to_csv(out_path, sep=",", index=False)
print(f"Saved cleaned file -> {out_path}")