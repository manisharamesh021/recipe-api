from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

#  Database connection
def get_db_connection():
    conn = sqlite3.connect("recipes.db")
    conn.row_factory = sqlite3.Row
    return conn


#  Pagination Route
@app.route("/recipes")
def get_recipes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 5))

    conn = get_db_connection()
    cursor = conn.cursor()

    offset = (page - 1) * limit
    cursor.execute("SELECT * FROM recipes LIMIT ? OFFSET ?", (limit, offset))

    recipes = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in recipes])


#  Filter Route (Empty if no filter)
@app.route("/filter")
def filter_recipes():
    country = request.args.get("country")

    if not country:
        return jsonify([])

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes WHERE country = ?", (country,))
    recipes = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in recipes])


#  MUST HAVE THIS
if __name__ == "__main__":
    app.run(debug=True)


@app.route("/count")
def count():
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM recipes")
    total = cursor.fetchone()[0]
    conn.close()
    return f"Total records: {total}"

if __name__ == "__main__":
    app.run(debug=True)