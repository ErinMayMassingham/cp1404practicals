from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"{celsius}°C is {fahrenheit:.2f}°F"
    except ValueError:
        return "Invalid input. Please enter a number."

if __name__ == '__main__':
    app.run()