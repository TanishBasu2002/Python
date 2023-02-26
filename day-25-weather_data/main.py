import pandas as pd
#data = pd.read_csv("weather_data.csv")
#data_dict = data.to_dict()
#print(data_dict)
# temp_list = data.temp.to_list()
#list_avg= sum(temp_list)/len(temp_list)
#avg = data.temp.mean()
#print("The avg of all numbers in the list is:", avg)
#print(data[data.temp == data.temp.max()])
#monday = data[data.day == "Monday"]
#farenhight = (int(monday.temp)*9/5)+32
#print(farenhight)
#create a dataframe
data_dict = {
    "student": ["tanish","kunal","arnab"],
    "scores": [99,55,20]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new.csv")
