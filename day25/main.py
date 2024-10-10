# with open("day25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     for i, d in enumerate(data):
#         data[i] = d.replace("\n", "")

# print(data)


# import csv

# with open("day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for i, row in enumerate(data):
#         if i == 0:
#             continue
#         temp.append(row[1])
#     print(temp)


# import pandas

# data: pandas.DataFrame = pandas.read_csv("day25/weather_data.csv")


# temp = data["temp"]

# # temp_list = temp.to_list()
# # print(sum(temp_list) / len(temp_list))

# # print(temp.max())


# # print(data[data.day == "Monday"])

# # print(data[data.temp == data.temp.max()])


# monday: pandas.DataFrame = data[data.day == "Monday"]
# print(monday.temp * (9 / 5) + 32)


import pandas

data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241007.csv")

fur_color = data["Primary Fur Color"]

x = fur_color.value_counts()

x.to_csv("day25/new_csv.csv")
