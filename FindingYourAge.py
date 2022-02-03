import datetime
year = datetime.date.today().year
user_age = int(input("What is your age?  "))
year = 2020
birth_year = int(year - user_age)
other_year = int(birth_year - 1)
print(f"You were born in either {birth_year} or {other_year}.")