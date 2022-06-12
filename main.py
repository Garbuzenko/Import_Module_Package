from application.db.people import get_employees
from application.salary import calculate_salary
import datetime

def date():
    print(f'date: {datetime.datetime.now()}')
if __name__ == '__main__':
    print("main")
    get_employees()
    calculate_salary()
    date()
