weather_data = [
    {"date": "2024-06-01", "max_temp": 28, "min_temp": 18, "humidity": 65},
    {"date": "2024-06-02", "max_temp": 29, "min_temp": 19, "humidity": 63},
    {"date": "2024-06-03", "max_temp": 27, "min_temp": 17, "humidity": 70},
    {"date": "2024-06-04", "max_temp": 30, "min_temp": 20, "humidity": 68},
    {"date": "2024-06-05", "max_temp": 26, "min_temp": 18, "humidity": 72},
    {"date": "2024-06-06", "max_temp": 28, "min_temp": 17, "humidity": 75},
    {"date": "2024-06-07", "max_temp": 31, "min_temp": 21, "humidity": 60},
    {"date": "2024-06-08", "max_temp": 29, "min_temp": 19, "humidity": 65},
    {"date": "2024-06-09", "max_temp": 27, "min_temp": 18, "humidity": 70},
    {"date": "2024-06-10", "max_temp": 28, "min_temp": 17, "humidity": 68},
    {"date": "2024-06-11", "max_temp": 30, "min_temp": 20, "humidity": 66},
    {"date": "2024-06-12", "max_temp": 29, "min_temp": 19, "humidity": 69},
    {"date": "2024-06-13", "max_temp": 27, "min_temp": 18, "humidity": 72},
    {"date": "2024-06-14", "max_temp": 28, "min_temp": 17, "humidity": 74},
    {"date": "2024-06-15", "max_temp": 31, "min_temp": 21, "humidity": 63},
    {"date": "2024-06-16", "max_temp": 29, "min_temp": 19, "humidity": 67},
    {"date": "2024-06-17", "max_temp": 28, "min_temp": 18, "humidity": 70},
    {"date": "2024-06-18", "max_temp": 30, "min_temp": 20, "humidity": 65},
    {"date": "2024-06-19", "max_temp": 27, "min_temp": 17, "humidity": 73},
    {"date": "2024-06-20", "max_temp": 29, "min_temp": 19, "humidity": 68},
    {"date": "2024-06-21", "max_temp": 28, "min_temp": 18, "humidity": 71},
    {"date": "2024-06-22", "max_temp": 30, "min_temp": 20, "humidity": 69},
    {"date": "2024-06-23", "max_temp": 27, "min_temp": 17, "humidity": 75},
    {"date": "2024-06-24", "max_temp": 28, "min_temp": 18, "humidity": 70},
    {"date": "2024-06-25", "max_temp": 29, "min_temp": 19, "humidity": 66},
    {"date": "2024-06-26", "max_temp": 31, "min_temp": 21, "humidity": 63},
    {"date": "2024-06-27", "max_temp": 28, "min_temp": 18, "humidity": 72},
    {"date": "2024-06-28", "max_temp": 32, "min_temp": 20, "humidity": 70},
    {"date": "2024-06-29", "max_temp": 27, "min_temp": 17, "humidity": 74},
    {"date": "2024-06-30", "max_temp": 29, "min_temp": 19, "humidity": 68},
    {"date": "2024-07-01", "max_temp": 30, "min_temp": 20, "humidity": 65},
    {"date": "2024-07-02", "max_temp": 28, "min_temp": 18, "humidity": 67},
    {"date": "2024-07-03", "max_temp": 27, "min_temp": 17, "humidity": 72},
    {"date": "2024-07-04", "max_temp": 29, "min_temp": 19, "humidity": 69},
    {"date": "2024-07-05", "max_temp": 30, "min_temp": 20, "humidity": 64},
    {"date": "2024-07-06", "max_temp": 28, "min_temp": 18, "humidity": 68},
    {"date": "2024-07-07", "max_temp": 27, "min_temp": 17, "humidity": 73},
    {"date": "2024-07-08", "max_temp": 29, "min_temp": 19, "humidity": 71},
    {"date": "2024-07-09", "max_temp": 31, "min_temp": 20, "humidity": 66},
    {"date": "2024-07-10", "max_temp": 28, "min_temp": 18, "humidity": 69}
]


def high_low(start_date):
    maxmin = []
    for data in weather_data:
        if data["date"] == start_date:
            index = weather_data.index(data)

            for i in range(7):
                maxmin.append(weather_data[index + i]["max_temp"])
                maxmin.append(weather_data[index + i]["min_temp"])
            return max(maxmin), min(maxmin)


def days_30():
    count = 0
    for data in weather_data:

        if data["max_temp"] > 30:
            count += 1
    return count



def humidity(date1,date2):
  humidity_list = []
  for data in weather_data:
    if date1 <= data["date"] <= date2:
      humidity_list.append(data["humidity"])
  if humidity_list:
    avg_humidity = sum(humidity_list) / len(humidity_list)
    return avg_humidity
  else:
    return "No data found for the given date range."