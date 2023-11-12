from flask import Flask, render_template, request, json
from flask_bs4 import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ghjghj^&*GHJ%^&*567867899iuyhgfgu%^&*IJHN'

# Przeniesienie arr, nazwiska, salary do zakresu globalnego
arr = []
arr2 = []
nazwiska = []
salary = None
min_salary = 0
max_salary = 0

total_salary = 0

@app.route('/')
def index():
    global arr, nazwiska, salary, total_salary, arr2, min_salary, max_salary
    arr = []
    # calculate_max_salary()
    # calculate_min_salary()
    nazwiska = []
    total_salary = 0
    arr2 = []  # Resetowanie arr2
    with open('salary.json') as salaryFile:
        salary = json.load(salaryFile)
        for y in salary:
            calculate_total_salary(salary[y].split(";"))
            arr.append(salary[y].split(";"))

    return render_template('index.html', title='Home', salary=salary, arr=arr, total_salary=total_salary, min_salary=min_salary, max_salary=max_salary)

@app.route('/getName', methods=['POST'])
def get_name():
    global arr, nazwiska, salary, total_salary
    last_name_filter = request.form.get('last_name', '').lower()
    filtered_arr = [row for row in arr if last_name_filter in row[1].casefold()]
    print(total_salary)
    print(last_name_filter)
    print(arr2)
    return render_template('index.html', title='Home', salary=salary, arr=filtered_arr, total_salary=total_salary, min_salary=min_salary, max_salary=max_salary)

def calculate_total_salary(data):
    global total_salary, min_salary, max_salary, arr2
    total_salary += int(data[3])
    arr2.append(int(data[3]))
    # print(arr2)
    sortedarr2 = sorted(arr2)
    print(sortedarr2[0])
    print(sortedarr2[-1])
    max_salary = sortedarr2[-1]
    min_salary = sortedarr2[0]
    if len(arr) > 0:
        total_salary = round ((sum(arr2) / len(arr)), 2)

# def calculate_min_salary():
#     global arr2, min_salary
#     min_salary = min(arr2)
#     print(min_salary)

# def calculate_max_salary():
#     global arr2, max_salary
#     max_salary = max(arr2)
#     print(max_salary)

if __name__ == '__main__':
    app.run(debug=True)
