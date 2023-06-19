#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string>')
def print_string(string):
    print(string)
    return string
@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(1, num + 1))
    return numbers
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = str(num1 + num2)
    elif operation == '-':
        result = str(num1 - num2)
    elif operation == '*':
        result = str(num1 * num2)
    elif operation == 'div':
        result = str(num1 / num2)
    elif operation == '%':
        result = str(num1 % num2)
    else:
        return 'Invalid operation'
    return result
if __name__ == '__main__':
    app.run()