from datetime import datetime

year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))

current_date = datetime.now()

birthdate = datetime(year, month, day)

age_in_seconds = (current_date - birthdate).total_seconds()

print(f"You are approximately {int(age_in_seconds)} seconds old.")
