import os
import random
from flask import Flask, jsonify
from dotenv import load_dotenv

# טעינת משתני הסביבה מהקובץ .env
load_dotenv()

app = Flask(__name__)


@app.route('/api')
def get_recipe():
    # שליפת שם המשתמש. אם לא קיים, נשתמש ב-Guest
    owner_name = os.getenv("USER_NAME", "Guest")

    # קריאת קובץ המלאי
    try:
        with open("inventory.txt", "r") as file:
            # קריאת השורות והתעלמות משורות ריקות
            ingredients = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        ingredients = []

    # לוגיקה פשוטה להצעת מתכון
    if not ingredients:
        suggestion = "Your fridge is empty. go to the supermarket!"
    else:
        chosen = random.choice(ingredients)
        suggestion = f"How about making something delicious with {chosen}?"

    # החזרת התשובה בפורמט JSON
    return jsonify({
        "greeting": f"Hello {owner_name}!",
        "inventory": ingredients,
        "suggestion": suggestion
    })


if __name__ == '__main__':
    # מריץ את השרת על פורט 5000 ופתוח לכל חיבור (0.0.0.0 חשוב לדוקר בהמשך)
    app.run(host='0.0.0.0', port=5000)