from flask import Flask

app = Flask(__name__)

@app.route('/prime_number/<number>')
def check_numbers(number):
    number = int(number)
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
    result = {
        "Number": number,
        "isPrime": is_prime,
    }
    return result

if __name__ == '__main__':
    app.run()