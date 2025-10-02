#! C:\Users\shirw\OneDrive\Documents\Practise\workShop2\workshop\Scripts\python.exe

import pandas as pd

# Load Titanic and keep only men
df = pd.read_csv("data/titanic.csv")
men = df.loc[df["Sex"] == "male"].copy()

# 1) Print first five names (as the exercise asks)
print(men["Name"].head())

# 2–4) Split Name -> LastName, Title, FirstName
#    Step A: split on the comma once: "Last, Title First"
last_rem = men["Name"].str.split(",", n=1, expand=True)
men["LastName"] = last_rem[0].str.strip()
rem = last_rem[1].str.strip()  # e.g., "Mr. Owen Harris"

#    Step B: split the remainder once on the first space
title_first = rem.str.split(" ", n=1, expand=True)
men["Title"] = title_first[0]
men["FirstName"] = title_first[1]

# 5) Drop the original Name column
men.drop(columns=["Name"], inplace=True)

# 6) Extract Deck as the first character of Cabin (NaN stays NaN)
men["Deck"] = men["Cabin"].str.get(0)

# Quick check
print(men[["LastName", "Title", "FirstName", "Cabin", "Deck"]].head(10))
