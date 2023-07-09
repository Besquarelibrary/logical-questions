import datetime


def count_days(year):
    days_count = {}

    for month in range(1, 13):
        for day in range(1, 32):
            try:
                # create a date object for the current day
                date = datetime.date(year, month, day)
                # get the day of the week as a string (e.g., "Monday")
                day_name = date.strftime("%A")
                # if the day name already exists as a key in the dictionary
                if day_name in day_counts:
                    # increment the count for that day
                    day_counts[day_name] += 1
                else:
                    day_counts[day_name] = 1
            except ValueError:
                # skip if the day is invalid for the given month
                continue

    return days_count


year_num = 2023
counts = count_days(year_num)

# Output the counts for each day of the week
for days, count in counts.items():
    print(days + ": " + str(count))
