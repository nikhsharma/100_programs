import datetime


def print_header():
    print('-----------------------------------')
    print('   HOW OLD ARE YOU IN SECONDS?')
    print('-----------------------------------')


def get_bday_from_user():
    print('When were you born? ')
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    return datetime.date(year, month, day)


def calculate_age_in_seconds(original_date, target_date):
    dt = original_date - target_date
    return -dt.days * 86400


def print_results(seconds):
    print("Looks like you\'re {} seconds old!".format(seconds))


def main():
    print_header()
    bday = get_bday_from_user()
    now = datetime.date.today()
    seconds = calculate_age_in_seconds(bday, now)
    print_results(seconds)


main()
