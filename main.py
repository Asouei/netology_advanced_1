
from package.application.salary import calculate_salary as c_s
from package.application.db.people import get_employees as g_e
import datetime

now = datetime.datetime.now()

if __name__ == '__main__':
    def main():
        print('Главный файл')
        c_s()
        g_e()
        print(f'Сейчас - {now}')

main()