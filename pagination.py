import sqlite3


def get_recipes(page, page_size):
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    offset = (page - 1) * page_size

    cursor.execute("""
        SELECT * FROM recipes
        LIMIT ? OFFSET ?
    """, (page_size, offset))

    rows = cursor.fetchall()
    conn.close()

    return rows


# ---- TEST PAGINATION ----
data = get_recipes(page=1, page_size=5)

for row in data:
    print(row)
