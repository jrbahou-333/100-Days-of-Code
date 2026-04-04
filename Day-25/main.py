import csv
import pandas

# with open("./weather_data.csv", mode="r") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# max = data.temp.max()
# print(data[data.temp == max])

# monday = data[data.day == "Monday"]
# mon_temp_c = monday.temp
# mon_temp_f = (mon_temp_c * (9/5)) + 32
# print(mon_temp_f)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ["Gray", "Cinnamon", "Black"]
colour_count = []
data_dict = {"Fur Color": colors}

for color in colors:
    count = len(data[data["Primary Fur Color"] == color])
    colour_count.append(count)

data_dict["Count"] = colour_count
print(data_dict)


new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_fur_color_count")