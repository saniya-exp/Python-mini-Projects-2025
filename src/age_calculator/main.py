from datetime import date

def calculate_age(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    print("🎂 Welcome to the Age Calculator 🎂")
    try:
        birth_year = int(input("Enter your birth year (YYYY): "))
        birth_month = int(input("Enter your birth month (MM): "))
        birth_day = int(input("Enter your birth day (DD): "))

        birth_date = date(birth_year, birth_month, birth_day)
        years, months, days = calculate_age(birth_date)

        print(f"\n✅ You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("❌ Invalid input! Please enter valid date numbers.")

if __name__ == "__main__":
    main()
