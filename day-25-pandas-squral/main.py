import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_count)
print(black_count)
print(red_count)
data_dict = {
    "Fur Color": ["Gray","Black","Red"],
    "Count": [gray_count,black_count,red_count]
}
print(data_dict)
df=pd.DataFrame(data_dict)
df.to_csv("Squiral_Count.csv")
