#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# ---registering routes---
# a resource available at "/".
# displays "Python Operations with Flask Routing and Views" in h1 in browser
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>", 200


# has a resource available at "/print/<parameter>"
# view should take one parameter, a string.
@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return f"{parameter}"


# should take one parameter, an integer.
# counts through range of parameter in "/count/<parameter" on separate lines
@app.route("/count/<int:parameter>")
def count(parameter):
    # return "".join([f"{num}\n" for num in range(0, parameter)])
    return "\n".join(str(i) for i in range(parameter)) + "\n"  # a trailing newline.

    # lines = []
    # for i in range(parameter):
    #     lines.append(str(i))
    # return "\n".join(lines) + "\n"

    # count = f""
    # for i in range(parameter):
    #     count += f"{i}\n"
    # return count


@app.route("/math/<int:num1>/<string:operation>/<int:num2>") #default is tring
def math(num1, operation, num2):
    if operation == "+":
        return str(num1 + num2)

    elif operation == "-":
        return str(num1 - num2)

    elif operation == "*":
        return str(num1 * num2)

    elif operation == "div":
        return str(num1 / num2)

    elif operation == "%":
        return str(num1 % num2)

    return "Operation not recognized. Please use one of the following: + - * div %"

@app.route("/math2/<num1>/<operation>/<num2>")
def math2(num1, operation, num2):
    if operation == "div": 
        operation = "/" #if operation is a div, covert it to "/" for divison
    return f"{eval(f'{num1} {operation} {num2}')}"  # fstrig converts the result to a string  and return it as the HTTP response.


if __name__ == "__main__":
    app.run(port=5555, debug=True)
