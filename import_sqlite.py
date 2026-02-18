import sqlite3
import json

with open("cleanedData.json", "r", encoding="utf-8") as f:
    data = json.load(f)


conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY,
    continent TEXT,
    country TEXT,
    cuisine TEXT,
    title TEXT,
    url TEXT,
    rating REAL,
    total_time INTEGER,
    prep_time INTEGER,
    cook_time INTEGER,
    description TEXT,
    calories INTEGER,
    carbohydrate INTEGER,
    cholesterol INTEGER,
    fiber INTEGER,
    protein INTEGER,
    saturated_fat INTEGER,
    sodium INTEGER,
    sugar INTEGER,
    fat INTEGER,
    servings INTEGER
)
""")

for recipe in data:
    cursor.execute("""
    INSERT INTO recipes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        recipe["id"],
        recipe["continent"],
        recipe["country"],
        recipe["cuisine"],
        recipe["title"],
        recipe["url"],
        recipe["rating"],
        recipe["total_time"],
        recipe["prep_time"],
        recipe["cook_time"],
        recipe["description"],
        recipe["calories"],
        recipe["carbohydrate"],
        recipe["cholesterol"],
        recipe["fiber"],
        recipe["protein"],
        recipe["saturated_fat"],
        recipe["sodium"],
        recipe["sugar"],
        recipe["fat"],
        recipe["servings"]
    ))

conn.commit()
conn.close()

print("Data successfully inserted into SQLite database!")
