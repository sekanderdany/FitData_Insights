def hourly_to_daily_step(hourly_steps):
    daily_steps = []
    for i in range(0, len(hourly_steps), 24):
        day_counts = sum(hourly_steps[i:i + 24])
        daily_steps.append(day_counts)
    return daily_steps

def choose_categories(steps):
    category = ""

    if steps < 5000:
        category = "concerning"
    elif 5000 <= steps < 10000:
        category = "average"
    else:
        category = "excellent"
    return category

data = ["Juliana",857,1178,1134,1133,780,1017,821,1180,0,0,0,0,0,0,0,1032,42,1129,1126,40,1032,743,1194,993,1054,969,1046,924,1064,1117,1094,795,0,0,0,0,0,0,44,26,47,736,22,46,851,27,846,769,1071,942,1010,1055,1011,834,1104,889,0,0,0,0,0,1120,38,1190,1100,959,874,1130,941,813,1106,934,1117,1043,1053,997,1055,1043,824,1183,908,0,0,0,0,0,0,0,937,1188,1145,747,1109,20,984,812,1059,742,739,926,1188,1072,1113,938,0,0,0,0,0,1067,26,29,45,722,796,32,28,36,1094,896,798,1101,963,928,829,842,1136,1115,0,0,0,0,0,0,0,27,769,26,1133,830,20,43,869,924,990,1000,963,768,1003,754,788,0,0,0,0,0,0,33,35,37,853,50,797,35,21,46,950,1099]

name = data[0]
hourly_steps = data[1:]
daily_steps = hourly_to_daily_step(hourly_steps)

daily_max = max(daily_steps)
daily_min = min(daily_steps)
daily_avg = sum(daily_steps)/len(daily_steps)

print(name + "'s daily steps:", daily_steps)
print("Summary stats for", name)
print("Max: ", daily_max)
print("Min: ", daily_min)
print("Average: ", daily_avg)

# Calling the function and printing the output
category = choose_categories(daily_avg)
print("Performance of", name, "this week:", category)