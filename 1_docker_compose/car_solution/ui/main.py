from flask import Flask, request, render_template_string, jsonify
import requests
import os

PORT = int(os.environ.get("PORT", 5000))
API_URL = os.environ.get("API_URL", "api") 
API_PORT = int(os.environ.get("API_PORT", 8000))

API_URL = f"http://{API_URL}:{API_PORT}"

app = Flask(__name__)

HTML = """
<form method='post'>
  Make: <input name='make'><br>
  Model: <input name='model'><br>
  Year: <input name='year' type='number'><br>
  <button type='submit'>Create Car</button>
</form>
<ul>
{% for car in cars %}<li>{{ car['make'] }} {{ car['model'] }} ({{ car['year'] }})</li>{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        car = {
            "make": request.form["make"],
            "model": request.form["model"],
            "year": int(request.form["year"]),
        }
        requests.post(f"{API_URL}/cars", json=car)
    cars = requests.get(f"{API_URL}/cars").json()
    return render_template_string(HTML, cars=cars)

# 🔁 Catch-all route
@app.route("/<path:path>")
def catch_all(path):
    return jsonify({"error": "CAR-UI - Route not found", "path": path}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)