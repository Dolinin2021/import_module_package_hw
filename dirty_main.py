from datetime import date
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_date = date.today()
    print(current_date)