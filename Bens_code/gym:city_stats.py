import json

data = [] 
with open("All_Gyms.json", "r") as json_data:
    for line in json_data:
        data.append(json.loads(line))

gyms_total = []
gyms_24hr = []
gym_ratios = []
gyms_per_capita = []
open24hr_per_capita = []

Cities = {"Los Angeles": 4030668, "New York City": 8580015, "Chicago": 2687682, "Dallas": 1359133, "Denver": 719116, "Philidelphia": 1573688, "Miami": 479009}


for row in data:
    if row["category"] == "all gyms":
        gyms_total.append(row["total"])
    else:
        gyms_24hr.append(row['total'])
