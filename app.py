from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Görev listesi (JSON formatında)
tasks = [
    {
        "order": 1,
        "id": "prepare-cream",
        "content": "Prepare the cream",
        "time": 15,
        "prerequisites": [],
        "chef_required": True,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 2,
        "id": "cool-cream",
        "content": "Let the cream cool",
        "time": 30,
        "prerequisites": ["prepare-cream"],
        "chef_required": False,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 3,
        "id": "prepare-ingredients",
        "content": "Bring all ingredients to room temperature",
        "time": 10,
        "prerequisites": [],
        "chef_required": False,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 4,
        "id": "mix-ingredients",
        "content": "Mix the ingredients for the dough",
        "time": 1,
        "prerequisites": ["prepare-ingredients"],
        "chef_required": True,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 5,
        "id": "knead-dough",
        "content": "Knead the dough",
        "time": 15,
        "prerequisites": ["mix-ingredients"],
        "chef_required": True,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 6,
        "id": "shape-dough",
        "content": "Shape dough into balls with cream inside",
        "time": 10,
        "prerequisites": ["knead-dough", "cool-cream"],
        "chef_required": True,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 7,
        "id": "preheat-oven",
        "content": "Preheat the oven to 180°C",
        "time": 15,
        "prerequisites": [],
        "chef_required": False,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 8,
        "id": "bake-cookies",
        "content": "Bake the cookies",
        "time": 20,
        "prerequisites": ["shape-dough", "preheat-oven"],
        "chef_required": True,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    },
    {
        "order": 9,
        "id": "add-powdered-sugar",
        "content": "Sprinkle powdered sugar on cookies",
        "time": 5,
        "prerequisites": ["bake-cookies"],
        "chef_required": False,
        "image": "https://img.freepik.com/premium-photo/celebrate-national-spicy-hermit-cookie-day-with-delicious-recipes_127934-105839.jpg?w=1380"
    }
]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)
