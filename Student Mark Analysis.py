import pandas as pd
import matplotlib.pyplot as plt

data = {
     "Name": ["Renisa", "Perlin" , "Vennila", "Xavier"],
     "Maths" : [85,95,78,86],
     "Science" : [79,85,67,85],
     "English" : [79,86,89,87]
     }

df = pd.DataFrame(data)

#Average
df["Average"] = df [["Maths","Science" ,"English"]].mean(axis=1)

#Pass or fail
df["Result"] = df ["Average"].apply(lambda x: "Pass" if x > 60 else "Fail")

print(df)

#Find the topper student
topper = df.loc[df ["Average"].idxmax()]
print("Topper:",topper["Name"])

#Find the lower student
lower = df.loc[df["Average"].idxmin()]
print("Lower:",lower["Name"])

#Provide Rank
df["Rank"] = df["Average"].rank(method="dense",ascending = False).astype(int)
print(df[["Name","Average","Rank"]])

#Sorting the Rank
df_sorted = df.sort_values(by = "Rank")
print(df_sorted[["Name","Average","Rank"]])

#Grading
def get_grade(avg):
    if avg>=80:
        return "A"
    elif avg>=75:
        return"B"
    elif avg>=60:
        return"C"
    elif avg>=50:
        return"D"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(get_grade)
print(df.head())

print("Number of students with A grade:",df[df["Grade"] == "A"].shape[0])

#Show grades in a Graph
df["Grade"].value_counts().plot(kind="bar",title="Grade Distribution")
plt.show()
