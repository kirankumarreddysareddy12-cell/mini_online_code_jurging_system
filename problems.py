def add_two_numbers(input_data):
    a, b = map(int, input_data.split())
    return str(a + b)

def reverse_string(input_data):
    return input_data[::-1]

def square_number(input_data):
    return str(int(input_data) ** 2)

def factorial_number(input_data):
    n = int(input_data)
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return str(fact)


PROBLEMS = {
    "sum": {
        "title": "Add Two Numbers",
        "solver": add_two_numbers
    },
    "reverse": {
        "title": "Reverse a String",
        "solver": reverse_string
    },
    "square": {
        "title": "Square of a Number",
        "solver": square_number
    },
    "factorial": {
        "title": "Find Factorial",
        "solver": factorial_number
    }
}

def get_problem(pid):
    return PROBLEMS[pid]
