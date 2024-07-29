from tempNYC import *
start_date = "2024-06-01"
date = "2024-07-04"

print("Question 1")

print(f"The highest and the lowest temperature recorded in a week starting from {start_date}: {high_low(start_date)}", )


print("-------------------------------------------------------------------------")

print("Question 2")

print(f"Number of days hotter than 30 degree Celcius: {days_30()} ")

print("-------------------------------------------------------------------------")

print("Question 3")

print(f"Average humidity from {start_date} to {date} is {humidity(start_date, date)}")


print("-------------------------------------------------------------------------")

