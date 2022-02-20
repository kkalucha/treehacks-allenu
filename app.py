from flask import Flask, render_template

app = Flask(__name__)

class Item:
    def __init__(self, name, price, description, severity):
        self.name = name
        self.price = price
        self.description = description
        self.severity = severity

class User:
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    test_user = User("Joe", ["Nuts", "Shrimp"])
    return render_template('user.html', user=test_user)

@app.route('/restaurant/<restaurant>')
def menu(restaurant):
    test_items = [
        Item("Shrimp Scampi", 24, "Shrimp sauteed in olive oil served with pasta", 2),
        Item("Caesar Salad", 14, "Caesar diff", 0),
        Item("Mushroom Soup", 16, "soup diff", 0),
        Item("Pepperoni Pizza", 18, "The House Special", 1)
    ]

    return render_template('menu.html', menu=test_items)
 
if __name__ == '__main__':
    app.run(debug=True)