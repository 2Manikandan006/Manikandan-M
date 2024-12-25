from datetime import date

def get_user_birthday():
    user_day = int(input("Enter your birth day: "))
    user_month = int(input("Enter your birth month: "))
    user_year = int(input("Enter your birth year: "))

    user_birthday = date(user_year, user_month, user_day)

    return user_birthday

def calculate_age(user_birthday):
    today = date.today()

    year_difference = today.year - user_birthday.year

    procedas_flag = ((today.month, today.day) < (user_birthday.month, user_birthday.day))

    #calculating the age

    age = year_difference - procedas_flag

    return age

user_birthday = get_user_birthday()
current_age = calculate_age(user_birthday)
print(f"The user's current age is: ", current_age)
