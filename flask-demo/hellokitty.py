from flask import Flask, render_template
from random import sample

cat = Flask(__name__, template_folder="templates", static_folder="static")

@cat.route("/")
def home() -> str:
    return "<h1>Hello Flask!</h1>"

@cat.route("/about")
def about_page() -> str :
    return render_template("/pages/about.html")

@cat.route("/lottery")
def lottery() -> str:
    lottery_numbers = number_generator(6)
    return render_template("lottery.html", lottery_numbers=lottery_numbers)

def number_generator(num: int) -> list[int]:
    numbers = range(1, 50)
    return sorted(sample(numbers, num))

if __name__ == "__main__":
    cat.run(port=9527, debug=True)