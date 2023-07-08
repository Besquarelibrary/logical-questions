import datetime

def count_days(year):
    day_counts = {}  # Initialize an empty dictionary to store the counts for each day of the week

    for month in range(1, 13):  # Iterate over all the months in the given year
        for day in range(1, 32):  # Iterate over all the days (up to 31) in each month
            try:
                date = datetime.date(year, month, day)  # Create a date object for the current day
                day_name = date.strftime("%A")  # Get the day of the week as a string (e.g., "Monday")
                if day_name in day_counts:  # If the day name already exists as a key in the dictionary
                    day_counts[day_name] += 1  # Increment the count for that day
                else:  # If the day name is encountered for the first time
                    day_counts[day_name] = 1  # Initialize the count to 1
            except ValueError:
                # Skip if the day is invalid for the given month (e.g., February 30)
                continue

    return day_counts

year = 2023
counts = count_days(year)  # Obtain the counts for each day of the week in the given year

# Output the counts for each day of the week
for day, count in counts.items():
    print(day + ": " + str(count))

